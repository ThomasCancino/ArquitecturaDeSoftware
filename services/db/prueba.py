import socket
import sys
import json

HOST = '192.168.1.20'
PORT = 5000
BUFFER_SIZE = 8192

def get_data(s, BUFFER_SIZE):
    data = b''
    while True:
        part = s.recv(BUFFER_SIZE)
        data += part
        if len(part) < BUFFER_SIZE:
            break

    return data

# 00010AAAAAHOLAS nnnnnSERVICIOCONTENIDO
def get_json():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect((HOST, PORT))
  
  s.sendall(b'00010sinitTROLL')
  data = get_data(s, BUFFER_SIZE)
  print(repr(data))
  
  
  s.sendall(b'00005HOLIS')
  data2 = get_data(s, BUFFER_SIZE)
  s.close()
  #data2 = s.recv(BUFFER_SIZE)
  data2 = data2.decode('utf-8')
  return json.loads(data2[12:])