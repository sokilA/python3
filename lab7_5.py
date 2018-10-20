#!/usr/bin/env python3

abc = list('aouiey')

def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string

def count_letter(string:str) -> str:
	''' counting letters '''
	count = 0
	for x in abc:
		count += string.count(x)
	return count

print(count_letter(input_string()))