// Список команд для датчика температуры
// Использование OneWire.write(0xCommand)

// Search Rom [F0h]:
// Когда система сначала включается, мастер должен идентифицировать коды ПЗУ всех подчиненных устройств на шине, 
// что позволяет мастеру определять количество ведомых устройств и их типы устройств. 
// Мастер изучает коды ПЗУ посредством процесса устранения, который требует, 
// чтобы мастер выполнял цикл поиска ROM (т. Е. Команду поиска ROM, за которой следует обмен данными) столько раз, 
// сколько необходимо для идентификации всех подчиненных устройств. Если на шине имеется только один ведомый, 
// более простая команда чтения ROM [33h] может использоваться вместо процесса поиска ROM. Подробное описание процедуры поиска ROM см. 
// В приложении «Примечание 937: Книга стандартов iButton®». 
// После каждого цикла поиска ROM мастер шины должен вернуться к шагу 1 (инициализация) в последовательности транзакций.
//
// Read Rom [33h]:
// Эта команда может использоваться только тогда, когда на шине есть один ведомый. 
// Он позволяет ведущему устройству считывать 64-битный код ПЗУ без использования процедуры поиска ROM. 
// Если эта команда используется, когда на шине присутствует более одного подчиненного устройства, 
// произойдет столкновение данных, когда все подчиненные попытаются ответить одновременно.
//
// Match Rom [55H]:
// Команда ПЗУ совпадения, за которой следует 64-битная последовательность кода ПЗУ, 
// позволяет ведущему устройству шины адресовать конкретное ведомое устройство на многоточечной или однодисковой шине.
// Только подчиненное устройство, которое точно соответствует кодовой последовательности 64-битного ПЗУ, будет отвечать на команду функции, 
// выдаваемую мастером; Все остальные ведомые устройства на шине будут ждать импульса сброса.
//
// Skip Rom [CCh]:
// Мастер может использовать эту команду для одновременного адресации всех устройств на шине без отправки какой-либо информации о кодах ПЗУ. 
// Например, мастер может заставить все DS18B20s на шине выполнять одновременные преобразования температуры,
// выдав команду Skip ROM, а затем команду Convert T [44h]. 
// Обратите внимание, что команда Read Scratchpad [BEh] может следовать команде Skip ROM только в том случае, если на шине имеется одно ведомое устройство. 
// В этом случае время сохраняется, позволяя мастеру читать из подчиненного устройства без отправки 64-битного кода ROM устройства. 
// Если вызвать команду Пропустить ПЗУ, а после вызвать команду прочитать Scratchpad, то это вызовет столкновение данных на шине, 
// если есть несколько подчиненных устройств, поскольку несколько устройств будут пытаться передавать данные одновременно.
//
// Alarm Search [ECh]:
// Работа этой команды идентична работе команды поиска ROM, за исключением того, 
// что будут отвечать только ведомые устройства с установленным сигналом тревоги. 
// Эта команда позволяет главному устройству определить, не возникло ли у какого-либо DS18B20s условие тревоги во время последнего температурного преобразования. 
// После каждого цикла поиска тревог (т. Е. Команды поиска сигнала, за которым следует обмен данными) ведущий сервер шины 
// должен вернуться к шагу 1 (инициализация) в последовательности транзакций. См. Раздел «Сигнализация Operation-Alarm Signaling» для объяснения операции флага тревоги.

// После того как мастер шины использовал команду ПЗУ для адреса DS18B20, с которой он хочет общаться, 
// мастер может выдать одну из функциональных команд DS18B20. Эти команды позволяют мастеру записывать и считывать данные из памяти блокнота DS18B20, 
// инициировать температурные преобразования и определять режим питания.

// Convert T [44h]:
// Эта команда инициирует одно преобразование температуры. 
// После преобразования результирующие тепловые данные сохраняются в 2-байтовом температурном регистре в памяти блокнотной памяти, 
// а DS18B20 возвращается в малое рабочее состояние холостого хода. 
// Если устройство используется в режиме питания от паразитов, в течение 10 мкс (макс.) 
// После выдачи этой команды мастер должен включить сильное подтягивание на 1-й шине на время преобразования (tCONV).
// Если DS18B20 питается от внешнего источника, мастер может выдавать интервалы времени считывания после команды Convert T, 
// и DS18B20 будет отвечать, передавая 0, пока выполняется преобразование температуры, и 1, когда выполняется преобразование. 
// В режиме питания паразитов этот метод уведомления не может быть использован, поскольку шина вытягивается высоко за счет сильного подтягивания во время преобразования.
//
// Write Scratchpad [4Eh]:
// Эта команда позволяет мастеру записывать 3 байта данных в блокнот DS18B20. 
// Первый байт данных записывается в регистр TH (байт 2 блокнота), второй байт записывается в регистр TL (байт 3), 
// а третий байт записывается в регистр конфигурации (байт 4). Сначала данные должны быть переданы младшим значащим бит. 
// Все три байта ДОЛЖНЫ быть записаны до того, как мастер выдает сброс, или данные могут быть повреждены.
//
// Read Scratchpad [BEh]:
// Эта команда позволяет мастеру прочитать содержимое блокнота. 
// Передача данных начинается с младшего значащего разряда байта 0 и продолжается через блокнот до тех пор, пока не будет прочитан 9-й байт (байт 8-CRC). 
// Мастер может выполнить сброс, чтобы прекратить чтение в любое время, если требуется только часть данных блокнотной памяти.
//
// Copy Scratchpad [48h]:
// Эта команда копирует содержимое блокнота TH, TL и конфигурационных регистров (байты 2, 3 и 4) в EEPROM. 
// Если устройство используется в режиме питания от паразитов, в течение 10 мкс (макс.) 
// После выдачи этой команды мастер должен включить сильное подтягивание на шине 1-Wire не менее 10 мс, как описано в разделе «Включение питания DS18B20».
//
// Recall E2 [B8h]:
// Эта команда вызывает значения триггера тревоги (TH и TL) и данные конфигурации из EEPROM и помещает данные в байтах 2, 3 и 4 соответственно 
// в память блокнотной памяти. Ведущее устройство может выдавать интервалы времени считывания после команды Recall E2,
// а DS18B20 будет указывать статус отзыва, передавая 0 во время повторного вызова и 1, когда вызов будет выполнен. 
// Операция отзыва происходит автоматически при включении питания, поэтому действительные данные доступны на блокноте сразу после подачи питания на устройство.
//
// Read Power Supply [B4h]:
// Ведущее устройство выдает эту команду, за которой следует временной интервал чтения, чтобы определить, 
// использует ли DS18B20s на шине мощность паразита. Во время временного интервала считывания DS18B20s с питанием от паразита вытащит шину на низком уровне, 
// а DS18B20s с внешним питанием позволят шине оставаться высокой. Информацию об использовании этой команды см. В разделе «Включение раздела DS18B20».

#include <OneWire.h>
OneWire  ds(2); // Создаём объект OneWire на 2-ом пине (нужен резистор в 4.7кОм)

// Заведём класс для датчик температуры
class TermoSensor
{
    byte addr[8]; // Номер нашего датчика
    boolean f; // Флаг, указывающий на то, включен он или нет
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
        f = false;
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

  
int prev_time;

void setup(void) 
{
    Serial.begin(115200);	// Начинаем последовательный вывод информации
    prev_time = millis();
}

void loop(void) 
{
    if (millis() - prev_time > 1000)
    {
        for (int i = 0; i < 16; i++)
            DS[i].Convert();
        delay (750);
        for (int i = 0; i < 16; i++)
            DS[i].getTemperature();
        for (int i = 0; i < 16; i++)
        {
            Serial.print("Senson number ");
            Serial.print(i + 1);
            Serial.print(" show ");
            Serial.print(DS[i].Temperature());
            Serial.println(" celsius!");
        }
    }  	
}

