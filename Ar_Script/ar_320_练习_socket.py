#encoding=utf-8

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8125))
sock.listen(10)

while 1:
    connection,address=sock.accept()
    buf=connection.recv(10)
    if not buf :break

    connection.send(b"received message")
sock.close()


#client
