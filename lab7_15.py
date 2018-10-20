#!/usr/bin/env python3 
import random

def input_length() -> int:
	''' Enter length of password '''
	pass_length = input('Enter length of password: ')
	return int(pass_length)

def generation_password(length_of_password:int) -> str:
	''' generat new password'''
	password = ''
	for x in range(length_of_password):
		password += random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*'))
	return password

print('Your password is - ' + generation_password(input_length()))