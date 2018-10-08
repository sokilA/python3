#!/usr/bin/env python3


brackets = ['(',')', '[',']','{','}','<','>'] 


def input_string() -> str:
	''' Enter start string '''
	entered_string = input('Enter your string: ')
	return entered_string


def check_couple_brackets(a:str) -> bool:
	counter = 0
	for x in brackets:
		counter += a.count(x)
	if (counter % 2) == 0:
		return False
	else:
		return True


def remove_characters(a:str) -> str:
	'''check couple of brackets and remove characters'''
	if check_couple_brackets(a):
		return 'false'

	for x in a:
		if x not in brackets:
			new_string = a.replace(x,"")
	return new_string


def check_right_of_brackets(a:str) -> bool:
	a = remove_characters(a)
	if a == 'false':
		return False
	couple_brackets = ['()','{}','<>','[]']
	while len(a) > 0:
		startLen = len(a)
		for x in couple_brackets:
			if x in a:
				a = a.replace(x, "")
			if len(a) == 0:
				return True
		if startLen == len(a):
			break
	return False



print(check_right_of_brackets(input_string()))