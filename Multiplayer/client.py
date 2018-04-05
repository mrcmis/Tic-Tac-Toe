import socket
import re

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1000

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.connect((TCP_IP, TCP_PORT))
data = ''

while not data == "closed":
    data = sockt.recv(BUFFER_SIZE).decode('utf-8')
    if data == "Write your name" or data == "Choose a row: " or data == "Choose a column: ":
        sockt.send(input(data).encode())
    else:
        print(data)
        sockt.send("ok".encode())