import socket
import sys
import json
import ast

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
def get_all():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect((HOST, PORT))
  
  s.sendall(b'00010sinitCLIEN')
  get_data(s, BUFFER_SIZE)
  #print(data.decode('utf-8'))
  
  
  s.sendall(b'00005SERV1')
  data2 = get_data(s, BUFFER_SIZE)
  s.close()
  #data2 = s.recv(BUFFER_SIZE)
  data2 = data2.decode('utf-8')
  print(data2)
  print()
  data2 = ast.literal_eval(data2[12:])
  
  for i in range(0, len(data2)):
      print(data2[i][0], data2[i][1])

def add_post(data):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect((HOST, PORT))
  
  s.sendall(b'00010sinitCLIEN')
  get_data(s, BUFFER_SIZE)
  #print(data.decode('utf-8'))
  
  s.sendall(bytes("00005SERV2" + data, 'utf-8'))
  data2 = get_data(s, BUFFER_SIZE)
  print(data2.decode('utf-8'))
  s.close()
  #data2 = s.recv(BUFFER_SIZE)
  #print(data2)
  #print()
  #data2 = ast.literal_eval(data2[12:])

print("¡Bienvenido! , ¿qué deseas hacer?")
print()
while True:
  print("1.- Ver publicaciones")
  print("2.- Crear publicación")
  print()
  while True:
      x = input()
      print()
      if x == "1":
          get_all()
          print()
          break
      elif x == "2":
        print ("Ingrese contenido")
        t = input()
        print()
        while True:
          if t != "":
            add_post(t)
            print("¡Listo!")
            print()
            break
        print()
        break
      else:
        print("Entrada inválida")
        print()
        break