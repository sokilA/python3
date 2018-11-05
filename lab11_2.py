#!/usr/bin/env python3

def start_number() -> str:
	number = input('enter your number - ')
	return number

def generate_random_num(number:str) -> str:
	while True:
		y = number[3:6] + number[0:3]
		mult = str(int(number)*int(y))
		if len(mult) > 6:
			mid = int(len(mult)/2)
			x = mult[mid-3:mid+3]
		else:
			x = mult
		while True:
			if x[0] == '0':
				x = x[1:]
			else:
				break
		number = x
		yield x



def start():
	num = start_number()
	x = generate_random_num(num)
	for i in x:
		print(i)
		state = input('write next or stop - ')
		if state == 'stop':
			break


start()









