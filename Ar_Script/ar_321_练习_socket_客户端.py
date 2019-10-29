
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8125))
while 1:
    msg=input("请输入你要发送的消息:").strip()
    if msg=='':
        continue
    if msg=='exit':
        break
    sock.sendall(b'123')
    data=sock.recv(1024)
    print("received:",data.decode())
sock.close()