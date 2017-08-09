import socket
import serial
import random
from threading import Thread
from queue import Queue

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

#ser = serial.Serial('/dev/ttyACM0',9600)

class RecieverPost(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

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
