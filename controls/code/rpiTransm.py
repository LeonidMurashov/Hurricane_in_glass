import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

def sendMsg(msg):
    s.sendto(bytes('t: '+msg, 'utf-8'),('255.255.255.255', 11719))

def getMsg():
    msg = s.recv(128)
    msg = msg.decode('utf-8')
    if not msg.startswith("r: "):
        return getMsg()
    else:
        return msg[3:]

def turnOn():
    sendMsg('set On=1')
    print("Модель включена!")

def turnOff():
    sendMsg('set On=0')
    print("Модель выключена!")

def getSensor(num):
    sendMsg('get S{}'.format(num))
    temp = getMsg()
    print("Температура {} : {}".format(num, temp))
    return temp

def getEnergy():
    sendMsg('get E')
    enrg = getMsg()
    print("Энергия: {}".format(enrg))
    return enrg
