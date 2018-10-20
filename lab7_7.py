#!/usr/bin/env python3

def input_variant():
	''' check which type you choose '''
	variant_num = int(input('Enter 1- If you want to replace from camel case to snake case \n2- If vice versa: '))
	return variant_num

def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string

def snake_to_camel(string:str) -> str:
	''' transform from snake case to camel case  '''
	i=0
	while i < len(string):
		if string[i] == '_':
			string = string[:i] + string[i+1:i+2].capitalize() + string[i+2:]
		i += 1
	return string

upper_abc = 'ABCDEFGHIGKLMNOPQRSTUVYXWZ'
lower_abc = 'abcdefghigklmnopqrstuvyxwz'

def camel_to_snake(string:str) -> str:
	''' transform from camel case to snake case  '''
	i=0
	while i < len(string):
		if string[i] in upper_abc:
			index = upper_abc.index(string[i])
			string = string[:i] + '_' + lower_abc[index] + string[i+1:]
		i += 1
	return string

variant = input_variant()
if variant == 1:
	print(camel_to_snake(input_string()))
elif variant == 2:
	print(snake_to_camel(input_string()))
else:
	print('You need enter only 1 or 2')

	