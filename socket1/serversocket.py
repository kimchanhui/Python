import time
import threading
from socket import *


def send(sock) :
    while True :
        sendData = input('>>>')
        connectionSock.send(sendData.encode('utf-8'))

def receive(sock) :
    while True :
        recvData = connectionSock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8080


serverScok = socket(AF_INET, SOCK_STREAM)
serverScok.bind(('', port))
serverScok.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverScok.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True :
    time.sleep(1)
    pass









