// Класс нагрузка -- стандартный класс приборов, управляемых ШИМом
class Load
{
	int pin; // Номер ШИМ-пина для ТВЭЛа
	int power; // Мощность ТВЭЛа (0..255)
	char msg[65]; // Сообщение приходящее от Rasbery для установки мощности
	int len; // Длина этого сообщения

	public:
	// Конструктор
	Load(int pin) 
	{
		this->pin = pin; // Устанавливаем соответсвующий пин
		pinMode(pin, OUTPUT); // PWM требует, чтобы пин был настроен на выход
		this->power = 0; // Ради безопасности при инициализации оставляем нагрузку выключенной
		analogWrite(pin, power); // Запускаем режим ШИМ
		msg[0] = '\0'; // Зануляем строку, чтобы убрать мусор
		len = 0;
	}

	// Функция обновления режима работы по Serial-запросу
	void Update(void)
	{
		// Если есть доступные данные считываем их и только тогда изменяем режим работы
		if ((len = Serial.available()) > 0) 
		{
			delay(5);
			Serial.println(len);
			len = Serial.available();
			Serial.println("Updated leln = ");
			Serial.print(len);
        	for (int i = 0; i < len; i++)
        	{
        		msg[i] = Serial.read(); // Считываем строку
        		if (msg[i] == ' ' || msg[i] == '\n' || msg[i] == '\r')
        		{
        			msg[i] = '\0';
        			break;
        		}
        	}
        	power = atoi(msg);
        	Serial.println(power);
        	// Вырабатываем мощность на ШИМе
			analogWrite(pin, power);
			Serial.println("Power changed!");
		}
		
	}
};

Load TVEL_1(9);		// Объект класса нагрузки на 9 пину
Load TVEL_2(10);	// Объект класса нагрузки на 10 пину

void setup()
{
	Serial.begin(115200); // Инициализируем последовательный ввод
}

// В цикле будем постоянно спрашивать, а не нужно ли нам поменять подаваемую мощность
void loop() 
{
	TVEL_1.Update(); 
	TVEL_2.Update();
}
