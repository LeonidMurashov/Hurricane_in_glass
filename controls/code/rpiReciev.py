import socket
import serial
import random
<<<<<<< HEAD
import time
=======
from threading import Thread
from queue import Queue
>>>>>>> 41604d38ed57c935d039738feb943d1e182a2348

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

ser1 = serial.Serial('/dev/ttyUSB0',9600)
ser2 = serial.Serial('/dev/ttyUSB1',9600)

<<<<<<< HEAD
def msgResponce(msg):
    print(msg)
    ser1.write(bytearray(msg,'utf-8'))
    ser2.write(bytearray(msg,'utf-8'))
    if msg == "ping":
        responce = "pong"
    else:
        responce1 = ser1.readline()
        responce2 = ser2.readline()
        responce = responce1 if str(responce2)[2:-5] == '-1' else responce2 
        print(responce1, responce2)
        #responce = str(random.randint(1, 65536))
        print("clear responce:", str(responce)[2:-5])
    s.sendto(bytes('r: '+str(responce)[2:-5], 'utf-8'), ('255.255.255.255', 11719))
=======
class RecieverPost(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
>>>>>>> 41604d38ed57c935d039738feb943d1e182a2348

    def run(self):
        while True:
            msg = self.queue.get()
            msg = msg.decode('utf-8')
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
            self.queue.task_done()


class RecieverPre(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            msg = s.recv(128)
            self.queue.put(msg)

if __name__ == '__main__':
    pre = RecieverPre()
    post = RecieverPost()
    q = Queue

    pre.run(q)
    post.run(q)
