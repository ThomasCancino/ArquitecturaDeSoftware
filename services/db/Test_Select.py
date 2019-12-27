import socket
import sqlite3
import time
import json
import sys

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 4096

def get_data(s, BUFFER_SIZE):
    data = b''
    while True:
        part = s.recv(BUFFER_SIZE)
        data += part
        if len(part) < BUFFER_SIZE: # either 0 or end of data
            break

    return data

#def formatted_message(service: str, msg: str):
#    length = len(service + msg)
#    if len(service) != 5:
#        raise Exception('El largo del nombre del servicio debe ser igual a 5')
#    if len(msg) == 0:
#        raise Exception('Falta el mensaje')
#    if length > 99999:
#        raise Exception('Mensaje excede el largo de 99999 caracteres')
#    left_padding = '0'*(5 - len(f'{length}'))
#    return str.encode(left_padding + str(length) + service + msg)

def get_product_json(data):
	keys = ['id', 'name', 'country', 'date']
	json_object = []

	for elem in data:
		dic = {}
		for item in enumerate(keys):
			dic[item[1]] = elem[item[0]]
		json_object.append(dic)

	return json.dumps(json_object)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'00010sinitHOLIS')
    data = get_data(s, BUFFER_SIZE)
    print('Received1 ', data.decode('utf-8'))

    while True:
      data2 = get_data(s, BUFFER_SIZE)
      print('Received2 ', data2.decode('utf-8'))
      # time.sleep(5)

      conn = sqlite3.connect('Project.db')
      c = conn.cursor()

      if len(data2) == 10:
        c.execute("SELECT * FROM CLIENTS")

      aux1 = get_product_json(c.fetchall())
      aux2 = "00" + str(len(aux1)+5) + "HOLIS" + aux1 #HACERLO FUNCION PLSSSSSSSSSSSSSSS
      conn.commit()
      conn.close()
      
      # aux2 = bytes(aux2, 'utf-8')
      #print(aux2, type(aux2))     
      #print(sys.getsizeof(bytes(aux2, 'utf-8')))
      
      
      if aux2:
          #s.sendall(b'00010HOLISTAMOS')
          s.sendall(bytes(aux2, 'utf-8'))
    
    
    s.close()



#c.execute('''CREATE TABLE CLIENTS
#             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')