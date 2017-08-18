import socket
import serial
import random
import time
import threading as T
from queue import Queue

# Словари, с компонентами каждого Arduino
ser1Components = ['P', 'T', 'E']
ser2Components = ['TODO: FILLME']

BOD = 115200
<<<<<<< HEAD
overheating = False
=======
>>>>>>> c8be87225f4cd16e807d2ac77c1b571e49cc420e

# Инициализация сокетов
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

# Авторизация Arduino, возвращает 2 serial объекта
def auth():
    ser1, ser2 = None, None

    # Поиск нужных портов
    for i in range(9):
        try:
            ser1 = serial.Serial('/dev/ttyUSB'+str(i), BOD, timeout=1)
            break
        except:
            continue
    for i in range(i+1,9):
        try:
            ser2 = serial.Serial('/dev/ttyUSB'+str(i),BOD, timeout=1)
            break
        except:
            continue

    print(ser1)
    print(ser2)
    print('ports found')

    # Ошибка при неисправности одной из Arduino
    if ser1 is None or ser2 is None:
        # ADD: send signal
        raise Exception("Cannot connect USB's")

    # Поиск Arduino с набором компонентов 1
    time.sleep(2)
    ser1.write(bytearray('AUTH\r\n', 'utf-8'))
    auth1 = str(ser1.readline())
    print('auth1 {}'.format(auth1))
    ser2.write(bytearray('AUTH\r\n', 'utf-8'))
    auth2 = str(ser2.readline())
    print('auth2 {}'.format(auth2))
    if auth2[2:-5] == '1':
        ser2, ser1 = ser1, ser2

    return [ser1, ser2]

def simulate_overheat():
    global overheating
    print('Testing overheating.')
    overheating = True
    time.sleep(15)
    overheating = False

def msgResponce(msg):
    print(msg)
    # Выделение частей запроса
    mid = msg.split(":")[0]
    device = msg.split(":")[1].split(" ")[0]
    msg = msg[4:]
    print(device)
    try:
        if device == 'test_alarm':
            th = T.Thread(target=simulate_overheat)
            th.start()
            responce = ' '
        # Распределение запроса между Arduino
<<<<<<< HEAD
        elif device in ser1Components:
=======
        if device in ser1Components:
>>>>>>> c8be87225f4cd16e807d2ac77c1b571e49cc420e
            print('deivce found in ser1')
            ser1.write(bytearray(msg,'utf-8'))
            print('request 2 arduino sent, w8 4 responce')
            responce = str(ser1.readline())[2:-5]
            print(responce)
<<<<<<< HEAD
            responce = str(random.randint(0,100))
=======
>>>>>>> c8be87225f4cd16e807d2ac77c1b571e49cc420e
        elif device in ser2Components:
            print('device found in ser2')
            ser2.write(bytearray(msg,'utf-8'))
            print('request to arduino sent, w8 4 responce')
            #time.sleep(1)
            responce = ser2.readline()[2:-5]
            print(responce)
        elif device == 'ping':
            responce = 'pong'
        elif device == 'turn':
            ser1.write(bytearray(msg, 'utf-8'))
            ser2.write(bytearray(msg, 'utf-8'))
            responce = "{} {}".format(str(ser1.readline())[2:-5],
                    str(ser2.readline()[2:-5]))
        # Ошибка при неизвестном компоненте
        else:
            print('Unknown device: {}'.format(device))
            responce = '-1'
    # Ошибка при отсутствии подключения к Arduino
    except:
        print("Cannot connect to arduino")
        responce = '-1'
    
    if overheating and device == 'T':
        responce = '100'
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
            q.put(msg[2:])

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
