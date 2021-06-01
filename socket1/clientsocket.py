import time
import threading
from socket import *

def send(sock) :
    while True :
        sendData = input('>>>')
        clientSock.send(sendData.encode('utf-8'))

def receive(sock) :
    while True :
        recvData = clientSock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8080


clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('연결이 확인되었습니다,')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True :
    time.sleep(1)
    pass









