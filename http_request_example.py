import socket
import sys

def RECV(rType,HOST):

    message = rType+' / HTTP/1.1\r\nHost:'+URL+'\r\n\r\n\r\n'

    sbuff = bytes(message,encoding='utf-8')
    s.send(sbuff)#전송부분

    clean = bytes('',encoding='utf-8')#누적 버퍼
    while True:
        rbuff = s.recv(1024)#값이 없어질때까지 다시받음
        if not rbuff:
            break
        else:
            clean +=rbuff
        
    text = clean.decode()
    print(rType + '내용 수신\n'+text)
    







URL = str(sys.argv[1])#
if ((len(sys.argv) >= 3) or (len(sys.argv) <= 1)):#인자값이 이상하게 받을경우 오류메세지 출력
    print("실행파일 URL (ex:http_request_example www.naver.com) 의 형태로 다시 입력하세요.")
    quit()
    
    
    

try:#잘못된 URL혹은 인터넷 불량시 오류메세지출력.
    HOST = socket.gethostbyname(URL)
except socket.gaierror as error:
    print('주소를 가져올수가 없습니다.\n인터넷 연결 혹은 올바른 주소를 입력하세요\n',error)
    quit()
PORT = socket.getservbyname('http','tcp')

#소켓 생성
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#소켓 연결
s.connect((HOST,PORT))

RECV('GET',HOST)
s.close()

print('종료합니다.')

