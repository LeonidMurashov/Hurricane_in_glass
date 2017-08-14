import socket
import transmitter

# Инициализация сокетов
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

# Создание объектра трансмиттера
t = transmitter.Transmitter()

# Класс станции (самого макета)
class Station():
    def __init__(self):
        self.connection = False
        self.power = False
        self.pipes = []
        self.sensors = []
        self.heaters = []

    # Проверка подключения к rpi перед любыми действиями
    def checkConnection(self):
        error = "Connect the model before performing any actions"
        assert self.connection == True, error

    # Подключение к rpi (обмен сообщениями ping-pong)
    def connect(self):
        mid = t.sendMsg("ping")
        msg = t.getMsg(mid)
        assert msg == 'pong', 'Failed to connect to Raspberry'
        self.connection = True

    # Включение\выключение станции
    def setPower(self, pwr):
        self.checkConnection()
        power = int(pwr)
        if power == 1:
            t.turnOn()
        elif power == 0:
            t.turnOff()
        else:
            raise ValueError("Model power must be a boolean value")

    # Получение энергии
    def getEnergy(self):
        self.checkConnection()
        return int(t.getEnergy())


# Класс насоса
class Pipe():
    def __init__(self, station, pin):
        assert type(station) is Station, "Wrong argument type: {}".format(str(type(station)))
        station.checkConnection()
        station.pipes.append(self)
        self.pin = pin
        self.power = None

    # Задать мощность насоса
    def setPower(self, val):
        error = "Wrong value {}: must be between 0 and 100"
        assert val <= 100 and val>=0, error
        t.setPipe(self.pin, val)

    # Получить мощность насоса
    def getPower(self):
        return int(t.getPipe(self.pin))

# Класс датчика температуры
class Sensor():
    def __init__(self, station, pin):
        assert type(station) is Station, "Wrong argument type: {}".format(str(type(station)))
        station.checkConnection()
        station.sensors.append(self)
        self.pin = pin
        self.temperature = None

    # Получить значение с датчика
    def getValue(self):
        return int(t.getSensor(self.pin))

# Класс нагервателя
class Heater():
    def __init__(self, station, num):
        assert type(station) is Station, "Wrong argument type: {}".format(str(type(station)))
        station.checkConnection()
        self.num = num
        self.checkAvailible(station)

    # Проверка доступности нагревателя
    def checkAvailible(self, station):
        error1 = "Heater not availible"
        error2 = "Heater already exists"
        assert self.num == 0 or self.num == 1, error1
        for heater in station.heaters:
            assert self.num != heater.num, error2

    # Задать мощность на нагревателе
    def setPower(self, val):
        error = "Wrong value: {}, must be between 0 and 100".format(val)
        assert val <= 100 and val >= 0, error
        t.setHeater(self.pin, val)

    # Получить мощность на нагревателе
    def getPower(self):
        return int(t.getHeater(self.pin))
