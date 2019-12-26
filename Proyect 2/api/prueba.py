import socket
import sys

HOST = '200.14.84.235'
PORT = 5000
BUFFER_SIZE = 1024
# 00010AAAAAHOLAS nnnnnSERVICIOCONTENIDO

if (len(sys.argv) >= 2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))

    s.send(sys.argv[1])
    data = s.recv(BUFFER_SIZE)
    print(data)

    s.close()
