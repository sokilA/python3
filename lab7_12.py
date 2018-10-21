#!/usr/bin/env python3


def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string

def remove_unnecessary_spaces(string:str) -> str:
	return " ".join(string.split())

print(remove_unnecessary_spaces(input_string()))