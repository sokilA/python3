#!/usr/bin/env python3

def parse(file_name:str) -> int:
	with open(file_name, 'r') as nginx:
		for i in nginx:
			yield i.split()[9]


func = parse('2017_05_07_nginx.txt')
count = 0
for i in func:
	i = int(i)
	count += i

print(count)