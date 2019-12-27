import socket
import sqlite3
import time

HOST = '192.168.1.20'
PORT = 5000
BUFFER_SIZE = 8192

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'00010sinitSERV2')
    data = s.recv(BUFFER_SIZE)
    print('Received1 ', data.decode('utf-8'))

    while True:
      

      data2 = s.recv(BUFFER_SIZE)
      print('Received2 ', data2.decode('utf-8'))

      conn = sqlite3.connect('Project.db')  # You can create a new database by changing the name within the quotes
      c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
      data2 = data2.decode('utf-8')
      data2 = data2[10:]
      #print(data2, type(data2))
      params = (data2, 20)
      #print(params)
      #"INSERT INTO CLIENTS (Client_Name, Country_ID) VALUES ("+params[0]+", 20)"
      query = "INSERT INTO CLIENTS (Client_Name, Country_ID, Date) VALUES ('"+params[0]+"', 20, CURRENT_TIMESTAMP)"
      #print(query)
      c.execute(query)
      conn.commit()
      conn.close()
 
      if data2:
        s.sendall(b'00018SERV2SUCCESFULLY') 

s.close()




#c.execute('''CREATE TABLE CLIENTS
#             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')