#include <OneWire.h>
#include <Arduino.h>
#include <SoftwareSerial.h>
#include "DFRobotDFPlayerMini.h"
#include "FastLED.h"
#include "MsTimer2.h"
#include "DallasTemperature.h"

// Подсветка
#define LED_PIN     4
#define NUM_LEDS    55
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB

CRGB leds[NUM_LEDS]; //Инициализируем массив светодиодов
byte R = 0, G = 0, B = 0;

void Alarm(void);
void Readln(char * msg);
void shutdown(void);

OneWire  oneWire(2); // Создаём объект OneWire на 2-ом пине (нужен резистор в 4.7кОм)
DallasTemperature sensors(&oneWire);

const float seciruty_temp = 90; // Температура переграва системы безопасности
float user_temp = 1000; // Температура перегрева, которую устанавливает пользователь

// Заведём класс для датчик температуры
class TermoSensor
{
    DeviceAddress addr; // Номер нашего датчика
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
        sensors.setResolution(addr, 12);       
    }

    void getTemperature(void)
    {
        float buff;
        buff = sensors.getTempC(addr);
        if ((buff != 0.0)&&(buff != -127.0)) celsius = buff;
        // Если температура больше критической температуры безопасности или температуры установленной учениками, 
        if ((celsius >= seciruty_temp) || (celsius >= user_temp)) 
        {
            shutdown(); // и отключаем нагреватели
            Alarm(); // Включаем сигнализацию на 15 секунд
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
    TermoSensor(0x28, 0xFF, 0x90, 0x25, 0xA4, 0x16, 0x04, 0x41), //1 
    TermoSensor(0x28, 0xFF, 0xC2, 0xA6, 0x8A, 0x16, 0x03, 0xE5), //2
    TermoSensor(0x28, 0xFF, 0x11, 0x4E, 0xA4, 0x16, 0x04, 0x43), //3 
    TermoSensor(0x28, 0xFF, 0xB2, 0x0C, 0xA4, 0x16, 0x05, 0x87), //4
    TermoSensor(0x28, 0xFF, 0xBB, 0x0D, 0xA4, 0x16, 0x05, 0xFB), //5 
    TermoSensor(0x28, 0xFF, 0x76, 0xE0, 0x94, 0x16, 0x04, 0x61), //6 
    TermoSensor(0x28, 0xFF, 0xC8, 0x71, 0x92, 0x16, 0x05, 0x6D), //7 
    TermoSensor(0x28, 0xFF, 0x72, 0x60, 0xA4, 0x16, 0x04, 0x79), //8
    TermoSensor(0x38, 0xFE, 0x72, 0x62, 0xA4, 0x26, 0x74, 0x59), 
    TermoSensor(0x38, 0xFE, 0x72, 0x62, 0xA4, 0x36, 0x84, 0x29), 
    TermoSensor(0x28, 0xFF, 0xD3, 0xAF, 0xA1, 0x16, 0x04, 0x11), //11 Внутри рекатора 2 
    TermoSensor(0x28, 0xFF, 0x9F, 0x07, 0x93, 0x16, 0x04, 0xFD), //12 Внутри реактора 1 
    TermoSensor(0x28, 0xFF, 0x20, 0x96, 0xA4, 0x16, 0x04, 0x17), //13 машинный зал 2 энергоблок 
    TermoSensor(0x28, 0xFF, 0x29, 0xA2, 0x8A, 0x16, 0x03, 0x41), //14 вход реактора 2 
    TermoSensor(0x28, 0xFF, 0xA1, 0x9B, 0xA4, 0x16, 0x05, 0xD2), //15 машинный зал 1 энергоблок 
    TermoSensor(0x28, 0xFF, 0x30, 0x6C, 0x92, 0x16, 0x05, 0x50)  //16 вход реактора 1
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
    FastLED.setBrightness(255);
    FastLED.clear();

    // Устанавливаем прерывание по таймеру для подсветки
    MsTimer2::set(10, flash); // 10ms period
    
    Serial.begin(9600);
    Serial.println(1);

    // Датчики температуры
    sensors.begin();
    //Serial.print("There are ");
    //sensors.setResolution(9);
    sensors.setWaitForConversion(0);
    sensors.setCheckForConversion(1);
    //prev_time_1 = millis();

    delay(1000);
    MsTimer2::start(); // Начинаем светить
    Serial.println(1);
}

void loop()
{
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
                //Serial.println(atoi(msg));
                //Serial.println(Serial.peek());
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
             //           myDFPlayer.volumeUp();
                        error = 0; // Всё хорошо
                        break;
                    }

                    // Уменьшаем громкость
                    case '-':
                    {
              //          myDFPlayer.volumeDown();
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
                Alarm(); // Включили сирену на 15 секунда
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
       //                 myDFPlayer.reset();
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
            Serial.println(5);
    }
    
    // Запрос на обновлениие температуры
    if ((sensors.isConversionComplete()) && (millis() > prev_time_1 + 750)) // Если мы не обновляли температуру больше секунды
    {
        //sensors.requestTemperatures();
        prev_time_1 = millis(); // Обнулили последнее время получения температуры
        sensors.requestTemperatures();
        /*if (sensors.isConversionComplete())
        {
          for (int i = 0; i < 16; i++)
                DS[i].getTemperature();
        }*/
    }

    for (int i = 0; i < 16; i++)
        DS[i].getTemperature();

    
}

void Alarm(void)
{
    byte BR = R; // Красный
    byte BG = G; // Зелёный
    byte BB = B; // Голубой

    //Заполняем всё красным и мигаем 
    MsTimer2::stop();
    FastLED.setBrightness(255); // Установили подсветку
    MsTimer2::start();
//    MsTimer2::start();

    for (int i = 0; i < 20; i++)
    {
        R = 255; // Красный
        G = 0; // Зелёный
        B = 0; // Голубой
        MsTimer2::stop();
        fill_solid(leds, NUM_LEDS, CRGB(R, G, B));
        MsTimer2::start();
        delay(500);

        R = 0; // Красный
        G = 0; // Зелёный
        B = 0; // Голубой
        MsTimer2::stop();
        fill_solid(leds, NUM_LEDS, CRGB(R, G, B));
        MsTimer2::start();
        delay(500);
    }

    R = 0; // Красный
    G = 0; // Зелёный
    B = 0; // Голубой

    MsTimer2::stop();
    fill_solid(leds, NUM_LEDS, CRGB(R, G, B));
    MsTimer2::start();
    

 //   MsTimer2::stop(); // Запретили прерывание
 //   MsTimer2::set(10, flash); // Поменяли период на 10миллисекунд 100фпс
 //   MsTimer2::start(); // Разрешили прерывание
}

void Readln(char * msg)
{
    int i, k;
    int len;
    int b;
    delay(5);
    len = Serial.available();
    for (i = 0; i < len + 10; i++)
    {
       for(k = 0; k < 100; k++)
       {
          if (Serial.peek() != -1){
            msg[i] = Serial.read();
            break;
          }
       }
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
