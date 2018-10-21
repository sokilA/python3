#!/usr/bin/env python3


def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string

def sort_by_len(string:str):
	# Sort string according to length of word
	return ' '.join(sorted(string.split(), key=len, reverse=True))

print(sort_by_len(input_string()))