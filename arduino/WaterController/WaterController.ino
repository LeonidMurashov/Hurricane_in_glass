
volatile uint16_t Count_1 = 0, Count_2 = 0; // Определяем переменную для подсчёта количества импульсов поступивших от датчика
uint32_t Time_1 = 0, Time_2 = 0; // Определяем переменную для хранения времени последнего расчёта
int8_t  Result_1 = 0, Result_2 = 0; // Определяем переменную для хранения рассчитанной скорости потока воды

// Определяем функцию, которая будет приращать значение счётчика импульсов
void CountInt_1()
{
	Count_1++;
    Serial.println("CountInt_1!");
}

void CountInt_2()
{
    Count_2++;
    Serial.println("CountInt_2!");
}                             

void setup()
{
    Serial.begin(115200); // Инициируем передачу данных в монитор последовательного порта
    pinMode(2, INPUT); // Конфигурируем вывод к которому подключён датчик, как вход
    attachInterrupt(0, CountInt_1, RISING); // Назначаем функцию CountInt_1 как обработчик прерываний intSensor при каждом выполнении условия RISING - переход от 0 к 1
    pinMode(3, INPUT); // Конфигурируем вывод к которому подключён датчик, как вход
    attachInterrupt(1, CountInt_2, RISING); // Назначаем функцию CountInt_1 как обработчик прерываний intSensor при каждом выполнении условия RISING - переход от 0 к 1
}

void loop()
{
	// Если c момента последнего расчёта прошла 1 секунда, или произошло переполнение millis то ...
    if((Time_1 - millis()) > 1000)
    {           
        Result_1 = Count_1 / 7.5; // Рассчитываем скорость потока воды: Q = F/7,5 л/мин
        Count_1 = 0; // Сбрасываем счётчик
        Time_1 = millis(); // Сохраняем время расчёта
    }                                                          // (количество импульсов от датчика varCount равно частоте в Гц, так как расчёт происходит 1 раз в секунду)
    Serial.println((String) "CKOPOCTb = "+Result_1+" L/MIN"); // Выводим скорость потока воды, показания которой будут меняться 1 раз в секунду
    // Если c момента последнего расчёта прошла 1 секунда, или произошло переполнение millis то ...
    if((Time_2 - millis()) > 1000)
    {           
        Result_2 = Count_1 / 7.5; // Рассчитываем скорость потока воды: Q = F/7,5 л/мин
        Count_2 = 0; // Сбрасываем счётчик
        Time_2 = millis(); // Сохраняем время расчёта
    }
    Serial.println((String) "CKOPOCTb = "+Result_2+" L/MIN"); // Выводим скорость потока воды, показания которой будут меняться 1 раз в секунду
}