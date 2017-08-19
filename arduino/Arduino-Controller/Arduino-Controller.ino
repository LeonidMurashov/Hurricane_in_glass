#include <OneWire.h>
#include <Arduino.h>
#include <SoftwareSerial.h>
#include "DFRobotDFPlayerMini.h"

// Инициализируем софтварные компорт и mp3 плеер
SoftwareSerial mySoftwareSerial(7, 8); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

void Readln(char * msg);
OneWire  ds(2); // Создаём объект OneWire на 2-ом пине (нужен резистор в 4.7кОм)
void shutdown(void);

// Заведём класс для датчик температуры
class TermoSensor
{
    byte addr[8]; // Номер нашего датчика
    byte f_temper; // Флаг, отвечающий за температурный режим [0..3]
    byte data[12]; // Массив данных
    float celsius; // Переменная, в которую мы будем класть значение температуры с датчика

public:
    // Конструктор
    TermoSensor(byte _1, byte _2, byte _3, byte _4, byte _5, byte _6, byte _7, byte _8)
    {
        addr[0] = _1;
        addr[1] = _2;
        addr[2] = _3;
        addr[3] = _4;
        addr[4] = _5;
        addr[5] = _6;
        addr[6] = _7;
        addr[7] = _8;
        f_temper = 0;
        celsius = -666;
    }

    void Convert(void)
    {
        // Перейдём к считыванию информации с датчиков
        ds.reset(); // Для начала сбросим наше устройство (вернёт 1, если подключено) 
        ds.select(addr); // Выберем наше устройство 
        ds.write(0x44); // Начинаем преобразование
        // Код 0x44 -- это команда выполнить температурную конверсию
    }

    void getTemperature(void)
    {
        ds.reset(); 
        ds.select(addr);    // Снова выбираем этот датчик
        ds.write(0xBE);         // Читаем его память (Scratchpad)

        for (int i = 0; i < 9; i++) // Нам нужно считать 9 байт         
            data[i] = ds.read();

        // Преобразуем данные в реальную температуру.
        int16_t raw = (data[1] << 8) | data[0];

        celsius = (float)raw / 16.0;
        if (celsius > 100)
        {
            f_temper = 3;
            shutdown();
        }
        else if (celsius > 75)
            f_temper = 2;
        else if (celsius > 50)
            f_temper = 1;
        else
            f_temper = 0;       
    }

    byte getF(void)
    {
        return f_temper;
    }

    float Temperature(void)
    {
        return celsius;
    }
};

// Мы знаем номер датчика и его серийный номер, поэтому заводим соответсвующий массив 
TermoSensor DS[16] = 
{
    TermoSensor(40, 255, 144, 37, 164, 22, 4, 65), 
    TermoSensor(40, 255, 32, 150, 164, 22, 4, 23), 
    TermoSensor(40, 255, 66, 71, 164, 22, 4, 11), 
    TermoSensor(40, 255, 161, 155, 164, 22, 5, 210), 
    TermoSensor(40, 255, 187, 13, 164, 22, 5, 251), 
    TermoSensor(40, 255, 118, 161, 164, 22, 5, 142), 
    TermoSensor(40, 255, 151, 72, 164, 22, 4, 29), 
    TermoSensor(40, 255, 21, 11, 164, 22, 5, 99), 
    TermoSensor(40, 255, 91, 156, 164, 22, 5, 79), 
    TermoSensor(40, 255, 114, 96, 164, 22, 4, 121), 
    TermoSensor(40, 255, 74, 86, 164, 22, 4, 130), 
    TermoSensor(40, 255, 17, 78, 164, 22, 4, 67), 
    TermoSensor(40, 255, 43, 131, 164, 22, 4, 222), 
    TermoSensor(40, 255, 7, 148, 164, 22, 4, 185), 
    TermoSensor(40, 255, 178, 12, 164, 22, 5, 135), 
    TermoSensor(40, 255, 118, 224, 148, 22, 4, 97)
};

// Класс нагрузка -- стандартный класс приборов, управляемых ШИМом
class Load
{
	int pin; // Номер ШИМ-пина для ТВЭЛа
	int power; // Мощность ТВЭЛа (0..255)
	char msg[65]; // Сообщение приходящее от Rasbery для установки мощности

	public:
	// Конструктор
	Load(int pin) 
	{
		this->pin = pin; // Устанавливаем соответсвующий пин
		pinMode(pin, OUTPUT); // PWM требует, чтобы пин был настроен на выход
		this->power = 0; // Ради безопасности при инициализации оставляем нагрузку выключенной
		analogWrite(pin, power); // Запускаем режим ШИМ
		msg[0] = '\0'; // Зануляем строку, чтобы убрать мусор
	}

    // Функция устанавливающая мощность [0, 1000]
    void setPower(int power)
    {
        this->power = power; // Устанавливаем мощность        
        analogWrite(pin, map(power, 0, 1000, 0, 255)); // Вырабатываем мощность на ШИМе
    }

	// Функция обновления режима работы по Serial-запросу
	void Update(void)
	{
		// Если есть доступные данные считываем их и только тогда изменяем режим работы
		if (Serial.available() > 0) 
		{
            Readln(msg); // Считываем слово
        	setPower(atoi(msg)); // Устанавливаем мощность в требуемом диапозоне
		}
	}

    // Функция возвращающая текущее значение мощности нагрузки
    int Power(void)
    {
        return power;
    }
};

Load TVEL[2] = {9, 10};		// Объект класса нагрузки на 9 и на 10пину
Load Pump(11); // Помпа на 11 пину

char msg[65]; // Сообщение приходящее от Rasbery для парсинга команд
unsigned long prev_time_1, prev_time_2; // Переменные для фонового обновления температуры
unsigned long prev_time_music; // Переменная для фонового обновления музыки 
byte folder = 0; // Определяем номер папки откуда мы играем музыку

void setup()
{
    mySoftwareSerial.begin(9600);
    Serial.begin(115200);
  
    Serial.println();
    Serial.println(F("DFRobot DFPlayer Mini Demo"));
    Serial.println(F("Initializing DFPlayer ... (May take 3~5 seconds)"));
  
    if (!myDFPlayer.begin(mySoftwareSerial)) 
    {  //Use softwareSerial to communicate with mp3.
        Serial.println(F("Unable to begin:"));
        Serial.println(F("1.Please recheck the connection!"));
        Serial.println(F("2.Please insert the SD card!"));
        while(true);
    }
    Serial.println(F("DFPlayer Mini online."));
  
    myDFPlayer.setTimeOut(500); //Set serial communictaion time out 500ms
  
    //----Set volume----
    myDFPlayer.volume(30);  //Set volume value (0~30).
//    myDFPlayer.volumeUp(); //Volume Up
//    myDFPlayer.volumeDown(); //Volume Down
  
    //----Set different EQ----
    myDFPlayer.EQ(DFPLAYER_EQ_NORMAL);
  
    //----Set device we use SD as default----
    myDFPlayer.outputDevice(DFPLAYER_DEVICE_SD);
  
  //----Mp3 control----
    //  myDFPlayer.sleep();     //sleep
    //  myDFPlayer.reset();     //Reset the module
    //  myDFPlayer.enableDAC();  //Enable On-chip DAC
    //  myDFPlayer.disableDAC();  //Disable On-chip DAC
    //  myDFPlayer.outputSetting(true, 15); //output setting, enable the output and set the gain to 15
  
    //----Mp3 play----
    myDFPlayer.play(1);  //Play the first mp3
    delay(30000);

    prev_time_1 = millis();
    prev_time_2 = millis();
    prev_time_music = millis();
}

void loop()
{
    static unsigned long timer = millis();
  
  if (millis() - timer > 30000) {
    timer = millis();
    myDFPlayer.next();  //Play next mp3 every 3 second.
  }
	// В цикле всегда пытаемся проверить, не пришла ли нам команда
	if (Serial.available() > 0) 
	{
		Readln(msg);
        // Дальше идёт много сравнений, чтобы определить, что есть что 
        // В силу наших определений можно всё определять по первой букве
        if (msg[0] == 'i') // isOn - узнать включен ли макет, 0/1
        {
        	// Если хотя бы одна помпа включена и один твел
        	if (TVEL[0].Power() || TVEL[1].Power() || Pump.Power()) 
        		Serial.println(1);
        	else
        		Serial.println(0);
        }
        else if (msg[0] == 't') // turn 0/1 - включить/выключить макет
        {
        	Readln(msg);
        	if (msg[0] == '0') // Выключаем макет
        	{
        		// Выключаем два нагревателя и помпы
        		TVEL[0].setPower(0);
        		TVEL[1].setPower(0);
        		Pump.setPower(0);
        	}
        	else if (msg[0] == '1')	// Включаем макет
        	{
        		// Реактор оставляем выключенным для безопасности
        		TVEL[0].setPower(0);
        		TVEL[1].setPower(0);
        		Pump.setPower(500);
        	}
        	else
        		Serial.println("-1");
        }
        else if (msg[0] == 'P') // P set/get # M - установить/получить мощность M на насосе #
        {
        	Readln(msg); // Читаем следующее слово
        	if (msg[0] == 's') // set
        	{
        		Readln(msg); // Читаем следующее слово
        		if (atoi(msg) == 6)
        			Pump.Update();
        	}
        	else if (msg[0] == 'g') // get
        	{
        		Readln(msg); // Читаем следующее слово
        		if (atoi(msg) == 6) // Шестая помпа
        			Serial.println(Pump.Power());
        	}
        	else
        		Serial.println("-1");
        }
        else if (msg[0] == 'H') // H set/get # M/ - установить/получить мощность M на кипятильнике #
        {
        	Readln(msg); // Читаем следующее слово
        	if (msg[0] == 's') // set
        	{
        		Readln(msg); // Читаем следующее слово
        		TVEL[atoi(msg) - 1].Update(); // Устанавливаем мощность
        	}
        	else if (msg[0] == 'g') // get
        	{
        		Readln(msg); // Читаем следующее слово
        		Serial.println(TVEL[atoi(msg) - 1].Power()); // Печатаем мощность
        	}
        	else
        		Serial.println("-1");
        }
        else if (msg[0] == 'E') // Запрашивается енергия
        {
        	// Обязательно нужна формула!!!
        	Serial.println(666);
        }
        else if (msg[0] == 'T') // Запрашивается температура
        {
        	Readln(msg); // Считываем номер датчика
        	Serial.println(DS[atoi(msg) - 1].Temperature()); // Печаетаем соответсвующую температуру
        }
        else
        	Serial.println("-1");
	}

    // Запрос на обновлениие температуры
	if (millis() - prev_time_1 > 1000) // Если мы не обновляли температуру больше секунды
    {
        for (int i = 0; i < 16; i++)
            DS[i].Convert(); // Отправляем запрос на конвертацию
        prev_time_1 = millis(); // Обнулили последнее время запроса на конвертацию
        prev_time_2 = millis(); // Обнулили последнее время получения температуры
    }

    // Забираем посчитанные данные
    if ((millis() - prev_time_1 > 750) || (millis() - prev_time_2 > 1000))
    {
    	for (int i = 0; i < 16; i++)
            DS[i].getTemperature();
        prev_time_2 = millis();
    }

    // Обновляем музыку в зависимости от температурного режима
    if (millis() - prev_time_music > 3000) //Проверяем температурный режим каждые 3 секунды
    {
        byte t;
        for (int i = 0; i < 16; i++)
            t = max (folder, DS[i].getF());
        if (t != folder)
        {
            folder = t;
            myDFPlayer.loopFolder(folder); //loop all mp3 files in folder SD:/xx.
        }
        prev_time_music = millis();
    }

}

void Readln(char * msg)
{
    int i;
    int len;
    delay(5);
    len = Serial.available();
    for (i = 0; i < len; i++)
    {
        msg[i] = Serial.read(); // Считываем строку
        if (msg[i] == ' ' || msg[i] == '\n' || msg[i] == '\r')
            break;
    }
    msg[i] = '\0';
}

void shutdown(void)
{
	// Выключаем два нагревателя
    TVEL[0].setPower(0);
    TVEL[1].setPower(0);
    delay(6000);
}