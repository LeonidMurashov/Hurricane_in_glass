import socket

# Инициализация сокетов
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

msg = ''
while msg != 'exit':
    msg = input()
    s.sendto(bytes('t AAA:'+msg, 'utf-8'), ('255.255.255.255', 11719))



