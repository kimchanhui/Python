from socket import *

def send(sock) :
    sendData = input('>>>')
    connectionSock.send(sendData.encode('utf-8'))

def receive(sock) :
    recvData = connectionSock.recv(1024)
    print('상대방 :', recvData.decode('utf-8'))


# socket 객체 생성 / 1 : 어드레스 패밀리, 2 : 소켓 타입
# 어드레스 패밀리 : 주소 체계 (인터넷에 사용되는 IP)
# AF_INET : IPv4 / AF_INET : IPv6 의미

serverScok = socket(AF_INET, SOCK_STREAM)  # 기본 모듈 불러오고 socket() 실행 > 소켓 생성
                                           # 생성한 소켓 bind : 클라이언트 X, 서버 O / 어드레스 패밀리 연결 과정
serverScok.bind(('', 8080))                # bind 함수 내에 '튜플' 입력 / bind('', 8080) X > bind(('', 8080))
                                           # 앞 : IP, 뒤 : Port / 앞 : ''(빈 문자열) 모든 인터페이스와 연결
serverScok.listen(1)                       # 서버 소켓에서만 사용 / 인자값 : 동시에 몇개의 동시접속 허용
                                           # 인자값을 입력하지 않을 경우 파이썬이 자의적으로 판단함

connectionSock, addr = serverScok.accept() # 소켓에 누군가가 접속하여 연결되었을 때에 결과가 return 되는 함수
                                           # 누군가가 접속을 하지 않으면 프로그램은 이 부분에서 멈춰있음
                                           # 접속하면 return 값으로 새로운 소켓과 상대방의 AF를 전달

print(str(addr), '에서 접속이 확인되었습니다.')

#data = connectionSock.recv(1024)
#print('받은 데이터 : ', data.decode('utf-8'))
#connectionSock.send('I am a server.'.encode('utf-8'))
#print('메세지를 보냈습니다.')

while True :
    send(connectionSock)

    receive(connectionSock)











