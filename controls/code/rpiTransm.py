import socket
from threading import Thread
import random
import time
import datetime

# Создание случайного номера запроса
from msgid import getMsgID

# Инициализация сокетов
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))
s.settimeout(1)

class Transmitter():
    def __init__(self):
        pass

    # Функция отправки запроса
    def sendMsg(self, msg):
        msgID = getMsgID()
        request = "t {}:{}".format(msgID, msg)
        s.sendto(bytes(request, 'utf-8'),('255.255.255.255', 11719))
        return msgID

    # Функция получения ответа на запрос по опр. msgID
    def getMsg(self, msgID):
        msg = ''
        search = "r {}:".format(msgID)
        try:
            while not msg.startswith(search):
                msg = s.recv(128)
                msg = msg.decode('utf-8')
            return msg[6:]
        except:
            return -1

    # Функции, отправляющие запросы на опр. действия на макет:

    def testAlarm(self):
        mid = self.sendMsg('test_alarm')

    def turnOn(self):
        mid = self.sendMsg('turn 1')
        code = self.getMsg(mid)
        print("Модель включена!")
        return code

    def turnOff(self):
        mid = self.sendMsg('turn 0')
        code = self.getMsg(mid)
        print("Модель выключена!")
        return code

    def getSensor(self, num):
        mid = self.sendMsg('T {}'.format(num))
        temp = self.getMsg(mid)
        print("Температура {} : {} C".format(num, temp))
        return temp

    def getEnergy(self):
        mid = self.sendMsg('E')
        enrg = self.getMsg(mid)
        print("Энергия: {}".format(enrg))
        return enrg

    def getFlow(self, num):
        mid = self.sendMsg("F {}".format(num))
        flow = self.getMsg(mid)
        print("Поток {}: {} л/с".format(num, flow))
        return flow

    def setPipe(self, num, val):
        mid = self.sendMsg("P {} set {}".format(num, val))
        code = self.getMsg(mid)
        print("SET Насос {} {}%".format(num, val*100))
        return code

    def getPipe(self, num):
        mid = self.sendMsg("P {} get".format(num))
        val = self.getMsg(mid)
        print("GET Насос {} {}%".format(num, val))
        return val

    def setHeater(self, num, val):
        mid = self.sendMsg("H {} set {}".format(num, val))
        code = self.getMsg(mid)
        print("SET Нагреватель {} {}%".format(num, val*100))
        return code

    def getHeater(self, num):
        mid = self.sendMsg("H {} get".format(num))
        val = self.getMsg(mid)
        print("GET Нагреватель {} {}%".format(num, val))
        return val

    def setLED(self, red, green, blue):
        mid = self.sendMsg("L {} {} {}".format(red, green, blue))
        code = self.getMsg(mid)
        return code
