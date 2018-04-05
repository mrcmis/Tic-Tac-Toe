import socket
from gameplay import Gameplay

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1000

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.bind((TCP_IP, TCP_PORT))
sockt.listen(1)

conn, addr = sockt.accept()
print(addr)

conn2, addr2 = sockt.accept()
print(addr2)

gameplay = Gameplay(conn, conn2)

gameplay.start()

conn2.send('closed'.encode())
conn2.recv(BUFFER_SIZE)
conn2.close()

conn.send('closed'.encode())
conn.recv(BUFFER_SIZE)
conn.close()