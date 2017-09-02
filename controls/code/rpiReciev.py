import socket
import serial
import random
import time
import threading as T
from queue import Queue
#import led

# Словари, с компонентами каждого Arduino
ser1Components = ['T', 'E', 'D', 'H', 'L', 'W', 'brightness', 'ALARM','volume', 'alarm']
ser2Components = ['P', 'F', 'C']

BOD = 9600
overheating = False
power = True
#led.init()
#led.blink(0,1,0)

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
            ser1 = serial.Serial('/dev/ttyUSB'+str(i), BOD, timeout=2)
            break
        except:
            continue
    for i in range(i+1,9):
        try:
            ser2 = serial.Serial('/dev/ttyUSB'+str(i),BOD, timeout=2)
            break
        except:
            continue

    print('ports found')

    # Ошибка при неисправности одной из Arduino
    if ser1 is None or ser2 is None:
        return

    # Поиск Arduino с набором компонентов 1
    time.sleep(2)
    ser1.write(bytearray('I', 'utf-8'))
    auth1 = str(ser1.readline())
    print('auth1 {}'.format(auth1))
    ser2.write(bytearray('I', 'utf-8'))
    auth2 = str(ser2.readline())
    print('auth2 {}'.format(auth2))
    if auth2[2:-5] == '1':
        ser2, ser1 = ser1, ser2

    return [ser1, ser2]

# Симуляция перегрева
def simulate_overheat():
    global overheating
    print('Testing overheating.')
    overheating = True
    time.sleep(15)
    overheating = False

def msgResponce(msg):
    global ser1,ser2
    ser1.reset_input_buffer()
    ser2.reset_input_buffer()
    #print(msg)
    # Выделение частей запроса
    mid = msg.split(":")[0]
    device = msg.split(":")[1].split(" ")[0]
    msg = msg[4:]
    #print(device)
    #print(msg)
    try:
        if device == 'test_alarm':
            th = T.Thread(target=simulate_overheat)
            th.start()
            responce = ' '

        # Распределение запроса между Arduino
        elif device in ser1Components or msg.startswith('P 6'):
            #t = time.time()
            #print('deivce found in ser1')
            ser1.write(bytearray(msg,'utf-8'))
            responce = str(ser1.readline())[2:-5]
            #print(responce)
            #print(time.time() - t)
            #print()
        elif device in ser2Components:
            #t = time.time()
            #print('device found in ser2')
            ser2.write(bytearray(msg,'utf-8'))
            responce = ser2.readline()
            #print(responce)
            #print(time.time() - t)
            #print()
        elif device == 'ping':
            responce = 'pong'
        elif device == 'turn':
            ser1.write(bytearray(msg, 'utf-8'))
            ser2.write(bytearray(msg, 'utf-8'))
            responce = str(ser1.readline())[2:-5]
        elif device == 'isOn':
            ser1.write(bytearray(msg, 'utf-8'))
            ser2.write(bytearray(msg, 'utf-8'))
            responce1 = str(ser1.readline())[2:-5]
            responce2 = str(ser2.readline())[2:-5]
            if responce1 == '1' or responce2 == '1':
                responce = '1'
            else:
                responce = '0'

        # Ошибка при неизвестном компоненте
        else:
            print('Unknown device: {}'.format(device))
            responce = '-1'
        #led.stop_blink()
    # Ошибка при отсутствии подключения к Arduino
    except:
        print("Cannot connect to arduino")
        #led.blink(1,1,0)
        responce = '-1'
        ser = auth()
        while ser is None:
            time.sleep(0.5)
            ser = auth()
        ser1, ser2 = ser[0], ser[1]
    if overheating == True and device == 'T':
        responce = '100.0'

    try:
        t = time.time()
        s.sendto(bytes('r {}:{}'.format(mid, responce), 'utf-8'),
                ('255.255.255.255', 11719))
        print("Sent! "+str(time.time() - t))
    except Exception as e:
        print(e)
        #led.blink(0,0,1)

# Функция, обрабатывающая сообщения из очереди
def worker(q, qk):
    while True:
        if not q.empty():
            msg = q.get()
            msgResponce(msg)
            q.task_done()
        if not qk.empty():
            msg = qk.get()
            msgResponce(msg)
            qk.task_done()

# Функция постоянного получения сообщений
def getMsg(q, qk):
    while 1:
        msg = s.recv(128)
        msg = msg.decode('utf-8')
        if msg.startswith("t "):
            q.put(msg[2:])
        elif msg.startswith("k "):
            qk.put(msg[2:])

if __name__ == '__main__':
    try:
        # Авторизация Arduino и получение Serial объектов
        print('authorizing...')
        ser = auth()
        while ser is None:
            #led.blink(1,0,0)
            print("Cannot connect Arduinos!")
            time.sleep(2)
            ser = auth()
        #led.stop_blink()
        ser1, ser2 = ser[0], ser[1]
        print('done!')
        # Создание очереди
        q = Queue()
        qk = Queue()
        print('starting threads')
        # Поток, отвечающий за непрерывное получение сообщений
        recieverThread = T.Thread(target=getMsg, args=([q, qk]))

        # Поток, отвечающий за выполнение запросов из очереди
        workerThread = T.Thread(target=worker, args=([q, qk]))

        # Поток, отвечвющий за выполнение запросов детей
        #workerKidThread = T.Thread(target=worker, args=([qk]))


        # Запуск потоков
        recieverThread.start()
        workerThread.start()
        #workerKidThread.start()
    except Exception as e:
        print(e)
        #led.dispose()
        exit()
