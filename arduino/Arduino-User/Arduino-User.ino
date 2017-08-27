void Readln(char * msg);

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

volatile uint16_t Count_1 = 0, Count_2 = 0; // Определяем переменную для подсчёта количества импульсов поступивших от датчика
unsigned long Time_1 = 0, Time_2 = 0; // Определяем переменную для хранения времени последнего расчёта
float Result_1 = 0, Result_2 = 0; // Определяем переменную для хранения рассчитанной скорости потока воды

// Определяем функцию, которая будет приращать значение счётчика импульсов
void CountInt_1(void)
{
	Count_1++;
}

void CountInt_2(void)
{
    Count_2++;
}             

Load Pump[5] = {5, 6, 9, 10, 11}; // Инициализировали нагрузку на этих пинах
char msg[65]; // Сообщение приходящее от Rasbery для парсинга команд

int error = 0; // Для парсера для возникновения ошибки

void setup()
{
	Serial.begin(115200);	// Начинаем последовательный вывод информации
    pinMode(2, INPUT); // Конфигурируем вывод к которому подключён датчик, как вход
    attachInterrupt(0, CountInt_1, RISING); // Назначаем функцию CountInt_1 как обработчик прерываний intSensor при каждом выполнении условия RISING - переход от 0 к 1
    pinMode(3, INPUT); // Конфигурируем вывод к которому подключён датчик, как вход
    attachInterrupt(1, CountInt_2, RISING); // Назначаем функцию CountInt_1 как обработчик прерываний intSensor при каждом выполнении условия RISING - переход от 0 к 1
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

        switch(msg[0])
        {
            // Авторизация
            case 'I':
            {
                Serial.println(2);
                break;
            }

            // isOn - узнать включен ли макет, 0/1
            case 'i':
            {
                // Если хоть одна помпа включена
                if (Pump[0].Power() || Pump[1].Power() || Pump[2].Power() || Pump[3].Power() || Pump[4].Power()) 
                    Serial.print(1);
                else
                    Serial.print(0);
                break;
            }

            // turn 0/1 - включить/выключить макет
            case 't':
            {
                Readln(msg);
                switch(msg[0])
                {
                    // Выключаем макет
                    case '0':
                    {
                        // Выключаем все помпы
                        for (int i = 0; i < 5; i++)
                            Pump[i].setPower(0);
                        error = 0; // Всё хорошо

                        break;
                    }

                    case '1':
                    {
                        // Включаем все помпы на половину мощности
                        for (int i = 0; i < 5; i++)
                            Pump[i].setPower(500);
                        error = 0; // Всё хорошо

                        break;
                    }

                    default:
                        error = -1; // Неправильно ввели команду
                }

                break;
            }

            // P set/get # M - установить/получить мощность M на насосе #
            case 'P':
            {
                Readln(msg); // Получаем номер насоса
                int number = atoi(msg);
                if ((number > 0) && (number < 6))
                {
                    number--;
                    Readln(msg); // Получаем режим
                    switch(msg[0])
                    {
                        // set
                        case 's':
                        {
                            Pump[number].Update();
                            error = 0; // Всё хорошо
                            break;
                        }

                        // get
                        case 'g':
                        {
                            Serial.println(Pump[number].Power());
                            break;
                        }

                        default:
                            error = -1; // Неправильно ввели команду
                    }
                }
                error = -1; // Неправильно ввели команду
            }

            // Запрашивается поток воды
            case 'F':
            {
                Readln(msg); // Считываем номер датчика
                switch(msg[0])
                {
                    // Первый
                    case '1':
                    {
                        Serial.println(Result_1); // Печатаем первый результат
                        break;
                    }

                    // Второй
                    case '2':
                    {
                        Serial.println(Result_2); // Печатаем второй результат
                        break;
                    }

                    default:
                        error = -1; // Неправильно ввели команду
                }
            }

            default:
                error = -1; // Неправильно ввели команду
        }

        if (error)
        {
            if (error == -1)
                Serial.println(-1);
        }
        else
            Serial.println(0);

	}
    // Если c момента последнего расчёта прошла 1 секунда
    if((millis() - Time_1) > 1000)
    {  
        Result_1 = (1000*Count_1/7.5)/(millis() - Time_1); // Рассчитываем скорость потока воды: Q = F/7,5 л/мин
        Count_1 = 0; // Сбрасываем счётчик
        Time_1 = millis(); // Сохраняем время расчёта
    }                                                          // (количество импульсов от датчика varCount равно частоте в Гц, так как расчёт происходит 1 раз в секунду)
    // Если c момента последнего расчёта прошла 1 секунда
    if((millis() - Time_2) > 1000)
    {
        Result_2 = (1000*Count_2/7.5)/(millis() - Time_2); // Рассчитываем скорость потока воды: Q = F/7,5 л/мин
        Count_2 = 0; // Сбрасываем счётчик
        Time_2 = millis(); // Сохраняем время расчёта
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