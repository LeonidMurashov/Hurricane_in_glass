#include <string.h> 
char msg[65]; // Сообщение приходящее от Rasbery для парсинга команд

void Readln(char * msg);

void setup()
{
  Serial.begin(11200);
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
        //	if (!Pump[0].Power() && !Pump[1].Power() && !Pump[2].Power() && !Pump[3].Power() && !Pump[4].Power()) // Если все помпы выключены
        	if (!TVEL[0].Power() && !TVEL[1].Power() && !Pump.Power()) // Если обе твелы выключены и одна помпа
        		Serial.print(0);
        	else
        		Serial.print(1);
        }
        else if (msg[0] == 't') // turn 0/1 - включить/выключить макет
        {
        	Readln(msg);
        	if (msg[0] == '0') // Выключаем макет
        	{
        		/* Выключаем все помпы
        		for (int i = 0; i < 5; i++)
        			Pump[i].setPower(0); */
        		// Выключаем два нагревателя и помпы
        		TVEL[0].setPower(0);
        		TVEL[1].setPower(0);
        		Pump.setPower(0);
        	}
        	else	// Включаем макет
        	{
        		/* Включаем все помпы на половину мощности
        		for (int i = 0; i < 5; i++)
        			Pump[i].setPower(500); */
        		// Реактор оставляем выключенным для безопасности
        		TVEL[0].setPower(0);
        		TVEL[1].setPower(0);
        		Pump.setPower(500);
        	}
        }
        else if (msg[0] == 'P') // P set/get # M - установить/получить мощность M на насосе #
        {
        	Readln(msg); // Читаем следующее слово
        	if (msg[0] = 's') // set
        	{
        		Readln(msg); // Читаем следующее слово
        		int i = atoi(msg); // i - номер насоса
        		i--;
        		Readln(msg); // Читаем следующее слово
        		int power = atoi(msg); // M - мощность
        	/*	if (i == 5)
        			Pump.setPower(power);*/
        		Pump[i].setPower(power);
        	}
        	else // get
        	{
        		Readln(msg); // Читаем следующее слово
        		int i = atoi(msg); // i - номер насоса
        		i--;
        	/*	if (i == 5)
        			Serial.println(Pump.Power(power));*/
        		Serial.println(Pump[i].Power(power));
        	}
        }
        else if (msg[0] == 'H') // H set/get # M/ - установить/получить мощность M на кипятильнике #
        {
        	Readln(msg); // Читаем следующее слово
        	if (msg[0] = 's') // set
        	{
        		Readln(msg); // Читаем следующее слово
        		int i = atoi(msg); // i - номер нагревателя
        		i--;
        		Readln(msg); // Читаем следующее слово
        		int power = atoi(msg); // M - мощность
        		TVEL[i].setPower(power); // Устанавливаем мощность
        	}
        	else // get
        	{
        		Readln(msg); // Читаем следующее слово
        		int i = atoi(msg); // i - номер нагревателя
        		i--;
        		Serial.println(TVEL[i].Power(power)); // Печатаем мощность
        	}
        }
        else if (msg[0] == 'E')
        {
        	// Обязательно нужна формула!!!
        	Serial.println(666);
        }
        else if (msg[0] == 'T')


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
