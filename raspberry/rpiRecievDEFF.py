import socket
import serial
import random
import time

DUMMY = '-1'
BAUD = 9600

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

ser1, ser2 = None, None
for i in range(4):
    try:
        ser1 = serial.Serial('/dev/ttyUSB'+str(i), BAUD) 
        break
    except:
        continue
for i in range(i+1,4):
    try:
        ser2 = serial.Serial('/dev/ttyUSB'+str(i),BAUD)
        break
    except:
        continue
if ser1 is None or ser2 is None:
    raise Exception("Cannot connect USB's")

     
def msgResponce(msg):
    print(msg)
<<<<<<< HEAD
    try:
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
    except:
        print("Cannot connect to arduino")
        responce = '-1'
    s.sendto(bytes('r: '+ responce, 'utf-8'), ('255.255.255.255', 11719))
=======
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
    return responce
>>>>>>> game_logic

 
def getMsg():
    while 1:
        msg = s.recv(128)
        msg = msg.decode('utf-8')
        if msg.startswith("t: "):
            return msg[3:]