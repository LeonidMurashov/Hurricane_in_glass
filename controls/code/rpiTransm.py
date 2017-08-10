import socket
from threading import Thread
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

class Transmitter():
    def __init__(self):
        pass

    def sendMsg(self, msg):
        s.sendto(bytes('t: '+msg, 'utf-8'),('255.255.255.255', 11719))

    def getMsg(self):
        msg = s.recv(128)
        msg = msg.decode('utf-8')
        if msg.startswith("t: "):
            return self.getMsg()
        else:
            return msg[3:]

    def turnOn(self):
        self.sendMsg('set On=1')
        print("Модель включена!")

    def turnOff(self):
        self.sendMsg('set On=0')
        print("Модель выключена!")

    def getSensor(self, num):
        self.sendMsg('get S{}'.format(num))
        temp = self.getMsg()
        print("Температура {} : {}".format(num, temp))
        return temp

    def getEnergy(self):
        self.sendMsg('get E')
        enrg = self.getMsg()
        print("Энергия: {}".format(enrg))
        return enrg
