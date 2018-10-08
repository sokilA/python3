#!/usr/bin/env python3



def input_string() -> str:
	''' Enter start string '''
	stringForLandslide = input('Enter your string: ')
	return stringForLandslide

def input_num() -> int:
	''' Enter number for landslide '''
	num = int(input('Enter your num: '))
	return num

def check_num_out_of_half_string(a:str,num) -> bool:
	''' check that number not bigger than half string '''
	if  num < int(len(a)/2):
		return False
	else:
		return True


def landslide(a:str, num) -> str:
	''' landslide string '''
	if check_num_out_of_half_string(a, num):
		return print('Your number is bigger than half string')

	half_string = int(len(a)/2)
	first_part = a[:half_string]
	second_part = a[half_string:]

	if num > 0:
		string = first_part[num:] + second_part + first_part[:num]
	else:
		string = second_part[num:] + first_part + second_part[:num]

	return string


print(landslide(input_string(), input_num()))



