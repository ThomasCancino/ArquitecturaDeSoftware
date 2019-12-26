import socket
import sqlite3
import time

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'00010sinitHOLIS')
    data = s.recv(1024)
    print('Received1 ', data.decode('utf-8'))

    while True:
      

      data2 = s.recv(1024)
      print('Received2 ', data2.decode('utf-8'))

      conn = sqlite3.connect('Project.db')  # You can create a new database by changing the name within the quotes
      c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
      
      c.execute("SELECT * FROM CLIENTS")
      aux = c.fetchall()
      aux = str(aux)
      print(aux)

      conn.commit()
      conn.close()

      if data2:
          s.sendall(b'00021HOLISRecibido Xooro')

s.close()




#c.execute('''CREATE TABLE CLIENTS
#             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')