import socket
import serial
import random
import time
import threading as T
from queue import Queue

# Словари, с компонентами каждого Arduino
ser1Components = ['P1', 'P2']
ser2Components = ['sP', 'P4']

BOD = 9600

# Инициализация сокетов
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

# Авторизация Arduino, возвращает 2 serial объекта
def auth():
    ser1, ser2 = None, None

    # Поиск нужных портов
    for i in range(4):
        try:
            ser1 = serial.Serial('/dev/ttyUSB'+str(i), BOD)
            break
        except:
            continue
    for i in range(i+1,4):
        try:
            ser2 = serial.Serial('/dev/ttyUSB'+str(i),BOD)
            break
        except:
            continue

    # Ошибка при неисправности одной из Arduino
    if ser1 is None or ser2 is None:
        # ADD: send signal
        raise Exception("Cannot connect USB's")

    # Поиск Arduino с набором компонентов 1
    ser1.write(bytearray('AUTH', 'utf-8'))
    ser2.write(bytearray('AUTH', 'utf-8'))
    auth1 = str(ser1.readline())
    auth2 = str(ser2.readline())
    if auth2 == '1':
        ser2, ser1 = ser1, ser2

    return [ser1, ser2]

def msgResponce(msg):
    print(msg)

    # Выделение частей запроса
    mid = msg.split(":")[0]
    device = msg.split(":")[1].split(" ")[0]

    try:
        # Распределение запроса между Arduino
        if device in ser1Components:
            ser1.write(bytearray(msg,'utf-8'))
            responce = str(ser1.readline())
        elif device in ser2Components:
            ser2.write(bytearray(msg,'utf-8'))
            responce = str(ser2.readline())
        elif device == 'ping':
            responce = 'pong'
        elif device == 'turn':
            ser1.write(bytearray(msg, 'utf-8'))
            ser2.write(bytearray(msg, 'utf-8'))
            responce = "{} {}".format(str(ser1.readline()),
                    str(ser2.readline()))
        # Ошибка при неизвестном компоненте
        else:
            print('Unknown device: {}'.format(device))
            responce = '-1'
    # Ошибка при отсутствии подключения к Arduino
    except:
        print("Cannot connect to arduino")
        responce = '-1'
    s.sendto(bytes('r {}:{}'.format(mid, responce), 'utf-8'),
            ('255.255.255.255', 11719))

# Функция, обрабатывающая сообщения из очереди
def worker(q):
    while True:
        msg = q.get()
        msgResponce(msg)
        q.task_done()

# Функция постоянного получения сообщений
def getMsg(q):
    while 1:
        msg = s.recv(128)
        msg = msg.decode('utf-8')
        if msg.startswith("t "):
            q.put(msg)[2:]

if __name__ == '__main__':
    # Авторизация Arduino и получение Serial объектов
    print('authorizing...')
    ser = auth()
    ser1, ser2 = ser[0], ser[1]
    print('done!')
    # Создание очереди
    q = Queue()
    print('starting threads')
    # Поток, отвечающий за непрерывное получение сообщений
    recieverThread = T.Thread(target=getMsg, args=([q]))

    # Поток, отвечающий за выполнение запросов из очереди
    workerThread = T.Thread(target=worker, args=([q]))

    # Запуск потоков
    recieverThread.start()
    workerThread.start()
