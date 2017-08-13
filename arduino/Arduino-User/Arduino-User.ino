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

Load Pump[5] = {5, 6, 9, 10, 11}; // Инициализировали нагрузку на этих пинах
char msg[65]; // Сообщение приходящее от Rasbery для парсинга команд

void setup()
{
	Serial.begin(115200);	// Начинаем последовательный вывод информации
    delay(1000);
    Serial.println("We are ready!");
}

void loop()
{
	// В цикле всегда пытаемся проверить, не пришла ли нам команда
	if (Serial.available() > 0) 
	{
		Readln(msg);
        // Дальше идёт много сравнений, чтобы определить, что есть что 
        // В силу наших определений можно всё определять по первой букве
        if (msg[0] == 'i') // isOn - узнать включен ли макет, 0/1
        {
        	// Если хоть одна помпа включена
        	if (Pump[0].Power() || Pump[1].Power() || Pump[2].Power() || Pump[3].Power() || Pump[4].Power()) 
        		Serial.print(1);
        	else
        		Serial.print(0);
        }
        else if (msg[0] == 't') // turn 0/1 - включить/выключить макет
        {
        	Readln(msg);
        	if (msg[0] == '0') // Выключаем макет
        	{
        		// Выключаем все помпы
        		for (int i = 0; i < 5; i++)
        			Pump[i].setPower(0); 
        	}
        	else	// Включаем макет
        	{
        		// Включаем все помпы на половину мощности
        		for (int i = 0; i < 5; i++)
        			Pump[i].setPower(500); 
        	}
        }
        else if (msg[0] == 'P') // P set/get # M - установить/получить мощность M на насосе #
        {
        	Readln(msg); // Читаем следующее слово
        	if (msg[0] == 's') // set
        	{
        		Readln(msg); // Читаем следующее слово
        		Pump[atoi(msg) - 1].Update();
        	}
        	else if (msg[0] == 'g') // get
        	{
        		Readln(msg); // Читаем следующее слово
        		Serial.println(Pump[atoi(msg) - 1].Power());
        	}
        }
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