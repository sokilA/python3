#!/usr/bin/env python3

abc = list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')

def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string

def encrypt(start_string:str) -> str:
	''' encrypt your string '''
	for x in start_string:
		start_string = start_string.replace(x,abc[abc.index(x)+1])
	return start_string


print(encrypt(input_string()))
