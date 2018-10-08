#!/usr/bin/env python3

def input_string() -> str:
	''' Enter start string '''
	entered_string = input('Enter your string: ')
	return entered_string

def check_that_string_is_palindrome(a:str) -> bool:
	''' function return true if string is palindrome '''
	a = a.lower()
	string = ''.join(e for e in a if e.isalnum())
	revers_string = string[::-1]
	if string == revers_string:
		return True
	else: 
		return False

print(check_that_string_is_palindrome(input_string()))