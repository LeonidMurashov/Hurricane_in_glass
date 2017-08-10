import socket
import serial
import random
import time

DUMMY = '-1'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

ser1 = serial.Serial('/dev/ttyUSB0',9600)
ser2 = serial.Serial('/dev/ttyUSB1',9600)

def msgResponce(msg):
    print(msg)
    ser1.write(bytearray(msg,'utf-8'))
    ser2.write(bytearray(msg,'utf-8'))
    if msg == "ping":
        responce = "pong"
    else:
        responce1 = str(ser1.readline())[2:-5]
        responce2 = str(ser2.readline())[2:-5]
        responce = responce1 if responce2 == DUMMY else responce2 
        print(responce1, responce2)
        #responce = str(random.randint(1, 65536))
        print("clear responce:", responce)
    s.sendto(bytes('r: '+ responce, 'utf-8'), ('255.255.255.255', 11719))

 
def getMsg():
    while 1:
        msg = s.recv(128)
        msg = msg.decode('utf-8')
        if msg.startswith("t: "):
            msgResponce(msg[3:])

if __name__ == '__main__':
    getMsg()
