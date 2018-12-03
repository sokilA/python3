#! /usr/bin/python3

import socket
from datetime import date
import calendar 


my_date = date.today()
day = calendar.day_name[my_date.weekday()]

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = '127.0.0.1'                           
port = 9999                                           
serversocket.bind((host, port))                                  
serversocket.listen(5)
print('the server is waiting for connection')

clientsocket, addr = serversocket.accept()      
print('Got a connection from {}'.format(addr)) 

clientsocket.send('What is your name?'.encode('utf-8'))
client_answer = clientsocket.recv(1024)
print(client_answer.decode('utf-8'))
clientsocket.send('Hello, '.encode('utf8') + client_answer + '\n'.encode('utf-8'))

while True:
	
	clientsocket.send('What are you interested in?'.encode('utf-8'))
	client_answer = clientsocket.recv(1024).decode('utf-8').lower().strip()
	if client_answer == 'what is your name?':
		clientsocket.send('I am Bot\n'.encode('utf-8'))
	elif client_answer == 'which is day now?':
		clientsocket.send(day.encode('utf-8') + '\n'.encode('utf-8'))
	elif client_answer == 'good bye':
		break
	else:
		clientsocket.send('incorrect question\n'.encode('utf-8'))

clientsocket.close()
serversocket.close()








