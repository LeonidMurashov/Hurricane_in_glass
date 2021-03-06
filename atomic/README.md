# Atomic - Python-библиотека для управления макетом ядерной электростанции
  
## Класс Station
Класс, репрезентующий макет электростанции.  
  
Методы класса:  
  
**Station.connect()** - подключение к макету  
**Station.setPower(bool)** - изменение состояния электростанции (включена/выключена)  
**Station.getEnergy()** - получение количества энергии, вырабатываемой на станации  
  
Переменные класса:  
  
**Station.pipes** - список насосов, подключенных к станции  
**Station.sensors** - список датчиков температуры, подключенных к станции  
**Station.flows** - список датчиков потока, подключенных к станции  
  
## Класс Pipe  
Класс, репрезентующий водяные насосы.  
> При инициализации объекта класса необходимо передать объект станции первым аргументом и номер насоса вторым.  

Методы класса:  
  
**setPower(int)** - задает мощность работы насоса (от 0 до 1)  
**getPower()** - возвращает текующую мощность работы насоса  
    
## Класс Sensor
Класс, репрезентующий датчики температуры.  
> При инициализации объекта класса необходимо передать объект станции первым аргументом и номер датчика вторым.  

Методы класса:  
  
**getValue()** - возвращает значение, считанное с датчика  
  
## Класс Heater
Класс, репрезентующий нагреватели.  
> При инициализации объекта класса необходимо передать объект станции первым аргументом и номер нагревателя (0 или 1) вторым.  
   
Методы класса:  
  
**setPower(int)** - задает мощность работы нагревателя (от 0 до 1)  
**getPower()** - возвращает текущую мощность работы нагревателя  
  
## Класс Flow
Класс, репрезентующий датчики потока.  
> При инициализации объекта класса необходимо передать объект станции первым аргументом и номер датчика вторым.  
  
Методы класса:  
  
**getFlow()** - возвращает текущее значение датчика потока воды  
