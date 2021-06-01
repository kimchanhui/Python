from socket import *

def send(sock) :
    sendData = input('>>>')
    clientSock.send(sendData.encode('utf-8'))

def receive(sock) :
    recvData = clientSock.recv(1024)
    print('상대방 :', recvData.decode('utf-8'))


# 서버와 다르게 bind, listen, accept 과정이 빠짐
# connect가 추가됨

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))   # 서버에 접속하기 위해 connect

print('연결이 확인되었습니다,')

#clientSock.send('I am a client'.encode('utf-8'))
#print('메세지를 전송했습니다.')
#data = clientSock.recv(1024)
#print('받은 데이터 : ', data.decode('utf-8'))

while True :
    receive(clientSock)

    send(clientSock)









