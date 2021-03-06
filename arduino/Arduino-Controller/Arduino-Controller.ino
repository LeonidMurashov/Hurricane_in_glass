#include <OneWire.h>
#include <Arduino.h>
#include <SoftwareSerial.h>
#include "DFRobotDFPlayerMini.h"
#include "FastLED.h"
#include "MsTimer2.h"

// Подсветка
#define LED_PIN     3
#define NUM_LEDS    54
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB

CRGB leds[NUM_LEDS]; //Инициализируем массив светодиодов
byte R = 0, G = 0, B = 0;

// Инициализируем софтварные компорт и mp3 плеер
SoftwareSerial mySoftwareSerial(8, 7); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

void Readln(char * msg);
OneWire  ds(2); // Создаём объект OneWire на 2-ом пине (нужен резистор в 4.7кОм)
void shutdown(void);

const float seciruty_temp = 95; // Температура переграва системы безопасности
float user_temp = 1000; // Температура перегрева, которую устанавливает пользователь

// Заведём класс для датчик температуры
class TermoSensor
{
    byte addr[8]; // Номер нашего датчика
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
        celsius = -666; // Сразу видно, что датчик температуры ещё не успел инициализироваться и подсчитать первую температуру
        
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
        // Если температура больше критической температуры безопасности или температуры установленной учениками, 
        if ((celsius >= seciruty_temp) || (celsius >= user_temp)) 
        {
            shutdown(); // и отключаем нагреватели
            Alarm(15000); // Включаем сигнализацию на 15 секунд
        }    
    }

    // Функция возвращающая температуру в градусах Цельсия
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
byte folder = 0; // Определяем номер папки откуда мы играем музыку

int error = 0; // Для парсера для возникновения ошибки

// Если по какой-то причине у нас не будет виден плеер, мы перезагружаем ардуину
void(* resetFunc) (void) = 0; // Объявляем функцию reset с адресом 0

// Функция обработки прерывания по таймеру для зажигания светодиодов
void flash (void)
{
    // Просто рисуем то, что нам нужно
    FastLED.show();
}

void setup()
{
    // Подсветка
    delay(1000);
    LEDS.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
    FastLED.setBrightness(128);
    FastLED.clear();

    // Устанавливаем прерывание по таймеру для подсветки
    MsTimer2::set(10, flash); // 10ms period

    mySoftwareSerial.begin(9600); // Инициализируем собственный порт для музыки 
    Serial.begin(115200);
  
    // Если мы не видим плеер, мы перезагружаем ардуину
    if (!myDFPlayer.begin(mySoftwareSerial)) 
        resetFunc(); // Вызываем reset
  
    myDFPlayer.setTimeOut(500); //Set serial communictaion time out 500ms
  
    // Устанавливаем звукна полную мощность
    myDFPlayer.volume(30);  //Set volume value (0~30).
//    myDFPlayer.volumeUp(); //Volume Up
//    myDFPlayer.volumeDown(); //Volume Down
  
    // Устанавливаем нормальные настройки эквалайзера
    myDFPlayer.EQ(DFPLAYER_EQ_NORMAL);
  
    // Устанавливаем устройство с которого производится чтение -- microSD
    myDFPlayer.outputDevice(DFPLAYER_DEVICE_SD);

    // Включаем наш режим проигрывания звука через внешние колонки
    myDFPlayer.enableDAC();  
  
  //----Mp3 control----
    //  myDFPlayer.sleep();     //sleep
    //  myDFPlayer.reset();     //Reset the module
    //  myDFPlayer.enableDAC();  //Enable On-chip DAC
    //  myDFPlayer.disableDAC();  //Disable On-chip DAC
    //  myDFPlayer.outputSetting(true, 15); //output setting, enable the output and set the gain to 15

    prev_time_1 = millis();
    prev_time_2 = millis();

    delay(6000);
    MsTimer2::start(); // Начинаем светить
}

void loop()
{
    // В цикле всегда пытаемся проверить, не пришла ли нам команда
    if (Serial.available() > 0) 
    {
        error = 1;
        Readln(msg);

        // Дальше идёт switch
        // В силу наших определений можно всё определять по первой букве

        switch (msg[0])
        {
            // Авторизация
            case 'I': 
            {
                Serial.println(1);
                break;
            }

            // isOn - узнать включен ли макет, 0/1
            case 'i':
            {
                // Если хотя бы одна помпа включена и один твел
                if (TVEL[0].Power() || TVEL[1].Power() || Pump.Power()) 
                    Serial.println(1);
                else
                    Serial.println(0);
                break;
            }

            // turn 0/1 - включить/выключить макет
            case 't':
            {
                Readln(msg);
                switch (msg[0])
                {
                    // Выключаем макет
                    case '0':
                    {
                        // Выключаем два нагревателя и помпы
                        TVEL[0].setPower(0);
                        TVEL[1].setPower(0);
                        Pump.setPower(0);
                        error = 0;
                        break;
                    }

                    // Включаем макет
                    case '1':
                    {
                        // Реактор оставляем выключенным для безопасности
                        TVEL[0].setPower(0);
                        TVEL[1].setPower(0);
                        Pump.setPower(500);
                        error = 0;
                        break;
                    }

                    default:
                        error = -1; // Значит неправильно написали команду
                }
                break;
            }

            // P set/get # M - установить/получить мощность M на насосе #
            case 'P':
            {
                Readln(msg); // Получаем номер насоса
                int number = atoi(msg);
                if (number == 6) // На Arduino_Controller только погружная помпа номер 6
                {
                    Readln(msg); // Получаем режим
                    switch (msg[0])
                    {
                        // set
                        case 's':
                        {
                            Pump.Update();
                            error = 0;
                            break;
                        }

                        // get
                        case 'g':
                        {
                            Serial.println(Pump.Power());
                            break;
                        }

                        default:
                            error = -1; // Значит неправильно написали команду
                    }
                }
                else
                    error = -1; // Значит неправильно написали команду
                break;
            }

            // H set/get # M/ - установить/получить мощность M на кипятильнике #
            case 'H':
            {
                Readln(msg); // Получаем номер кипятильника
                int number = atoi(msg);
                // Проверка на корректные значения номеров кипятильников
                if ((number < 3) && (number > 0))
                {
                    number--;
                    Readln(msg); // Получаем режим
                    switch (msg[0])
                    {
                        // set
                        case 's':
                        {
                            TVEL[number].Update(); // Устанавливаем мощность
                            Serial.println(0);
                            break;
                        }

                        // get
                        case 'g':
                        {
                            Serial.println(TVEL[number].Power()); // Печатаем мощность
                            break;
                        }

                        default:
                            error = -1; // Значит неправильно написали команду
                    }
                }
                else
                    error = -1; // Значит неправильно написали команду

                break;
            }

            // Запрашивается енергия
            case 'E':
            {
                Serial.println(1500 * (TVEL[0].Power() + TVEL[1].Power()));
                break;
            }

            // Запрашивается температура
            case 'T':
            {
                Readln(msg); // Считываем номер датчика
                Serial.println(DS[atoi(msg) - 1].Temperature()); // Печаетаем соответсвующую температуру
                break;
            }

            // Устанавливаем цвет подсветки
            case 'L':
            {
                Readln(msg);
                R = atoi(msg); // Красный
                Readln (msg);
                G = atoi(msg); // Зелёный
                Readln(msg);
                B = atoi(msg); // Голубой

                //Заполняем всё одним и тем же светом
                MsTimer2::stop();
                fill_solid(leds, NUM_LEDS, CRGB(R, G, B));
                MsTimer2::start();
                error = 0;
                break;
            }

            // Мигать или нет
            case 'W':
            {
                Readln(msg);
                switch(msg[0])
                {
                    // Мигаем
                    case '1':
                    {
                        MsTimer2::stop(); // Запретили прерывание
                        MsTimer2::set(100, flash); // Поменяли период на 100миллисекунд 10фпс
                        MsTimer2::start(); // Разрешили прерывание
                        error = 0;
                        break;
                    }

                    // Не мигаем
                    case '0':
                    {
                        MsTimer2::stop(); // Запретили прерывание
                        MsTimer2::set(10, flash); // Поменяли период на 10миллисекунд 100фпс
                        MsTimer2::start(); // Разрешили прерывание
                        error = 0;
                        break;
                    }

                    default:
                        error = -1;
                }

                break;
            }

            // Устанавливаем яркость подсветки
            case 'b':
            {
                Readln(msg); // Считали яркость подсветки
                MsTimer2::stop(); // Запретили прерывание
                FastLED.setBrightness(atoi(msg)); // Установили подсветку
                MsTimer2::start(); // Разрешили прерывание
                error = 0; // Значит всё хорошо
                break;
            }
            // Сливаем воду
            case 'D':
            {
                Pump.setPower(1000); // Мощность подводной помпы устанавливаем на максимум
                error = 0; // Значит всё хорошо
                break;
            }

            //ALARM M - установить температуру включения сирены
            case 'A':
            {
                Readln(msg); // Считываем считываем температуру пользовательской сирены
                user_temp = atoi(msg); // Установили новое значение пользовательской температуры включения сирены
                error = 0; // Всё хорошо
                break;
            }

            // Изменяем громкость
            case 'v':
            {
                Readln(msg); // Считваем команду
                switch (msg[0])
                {
                    // Увеличиваем громкость
                    case '+':
                    {
                        myDFPlayer.volumeUp();
                        error = 0; // Всё хорошо
                        break;
                    }

                    // Уменьшаем громкость
                    case '-':
                    {
                        myDFPlayer.volumeDown();
                        error = 0; // Всё хорошо
                        break;
                    }

                    default:
                        error = -1; // Значит неправильно написали команду
                }

                break;
            }

            //alarm - включить сирену на 15 секунд
            case 'a':
            {
                Alarm(15000); // Включили сирену на 15 секунда
                error = 0; // Всё хорошо
                break;
            }

            // reset
            case 'r':
            {
                Readln(msg); // Считываем arduino или mp3
                switch(msg[0])
                {
                    // Перезагружаем arduino
                    case 'a':
                    {
                        resetFunc(); // Вызываем reset
                        break; // Формально он не нужен
                    }

                    // Перезагружаем плеер
                    case 'm':
                    {
                        myDFPlayer.reset();
                        error = 0; // Всё хорошо
                        break;
                    }

                    default:
                        error = -1;
                }

                break;
            }

            default: 
                error = -1; // Значит неправильно написали команду
        }            

        if (error)
        {
            if (error == -1)
                Serial.println(-1);
        }
        else
            Serial.println(0);
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
    if ((millis() - prev_time_1 > 800) || (millis() - prev_time_2 > 1000))
    {
    	for (int i = 0; i < 16; i++)
            DS[i].getTemperature();
        prev_time_2 = millis();
    }
}

void Alarm(unsigned long time)
{
    myDFPlayer.play(1);
    myDFPlayer.enableLoop(); //enable loop.
    delay(time); // Сирена играет 15 секунд
    myDFPlayer.disableLoop(); //disable loop.
    myDFPlayer.pause(); // Останавливаем сирену
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
}
