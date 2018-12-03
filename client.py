#! /usr/bin/python3

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = '127.0.0.1'                           
port = 9999
s.connect((host, port))

while True:                             
	server_responce = s.recv(1024)
	print(server_responce.decode('utf-8'))
	a = input()
	s.send(a.encode('utf-8'))
	if a == 'good bye':
		s.close()
		break


	





