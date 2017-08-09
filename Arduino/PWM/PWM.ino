class TVEL
{
	int pin; // Номер ШИМ-пина для ТВЭЛа
	int power; // Мощность ТВЭЛа (0..255)
	char msg[65]; // Сообщение приходящее от Rasbery для установки мощности
	int len; // Длина этог сообщения

	public:
	TVEL(int pin) // Конструктор
	{
		this->pin = pin;
		pinMode(pin, OUTPUT);
		this->power = 0;
		analogWrite(pin, power);
		msg[0] = '\0';
		len = 0;
	}

	void Update(void)
	{
		if ((len = Serial.available()) > 0) // Если есть доступные данные
		{
			Serial.println(len);
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

TVEL TVEL_1(9);		// Объект класса TVEL на 9 пину
TVEL TVEL_2(10);	// Объект класса TVEL на 10 пину

void setup()
{
	Serial.begin(115200); // Инициализируем последовательный ввод
}

void loop() 
{
	delay(150);
	TVEL_1.Update();
	TVEL_2.Update();
}
