import socket
import serial
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

#ser = serial.Serial('/dev/ttyACM0',9600)

def msgResponce(msg):
    print(msg)
    if msg == "ping":
        responce = "pong"
    elif msg.startswith("get S"):
        responce = str(random.randint(1, 100))
    elif msg == "get E":
        responce = str(random.randint(1000, 3000))
    else:
        responce = None
    if responce is not None:
        s.sendto(bytes('r: '+responce, 'utf-8'), ('255.255.255.255', 11719))


def getMsg():
    while 1:
        msg = s.recv(128)
        msg = msg.decode('utf-8')
        if msg.startswith("t: "):
            msgResponce(msg[3:])

if __name__ == '__main__':
    getMsg()
