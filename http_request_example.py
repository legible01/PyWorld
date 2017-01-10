import socket



print('다음과 같이 URL을 입력하세요. ex:www.naver.com')
URL = input("input URL:")
HOST = socket.gethostbyname(URL)
PORT = socket.getservbyname('http','tcp')

#소켓 생성
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#소켓 연결
s.connect((HOST,PORT))

#헤드 내용 수신
message = 'HEAD / HTTP/1.1\r\nHost:'+URL+'\r\n\n'

sbuff = bytes(message,encoding='utf-8')
s.send(sbuff)

rbuff = s.recv(2048)


print('헤드 내용 수신\n'+ rbuff.decode())
#GET 내용 수신
message = 'GET / HTTP/1.1\r\nHost:'+URL+'\r\n\r\n'
sbuff = bytes(message,encoding='utf-8')
s.send(sbuff)

rbuff = s.recv(4096).decode()


print('GET 내용 수신\n'+ rbuff)


s.close()

print("종료합니다.")

