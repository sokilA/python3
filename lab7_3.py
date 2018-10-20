#!/usr/bin/env python3


brackets = ['(',')', '[',']','{','}','<','>'] 


def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string


def check_couple_brackets(starting_string:str) -> bool:
	''' Check that in string there are even number of brackets '''
	counter = 0
	for x in brackets:
		counter += starting_string.count(x)
	if (counter % 2) == 0:
		return False
	else:
		return True


def remove_characters(starting_string:str):
	'''check couple of brackets and remove characters'''
	if check_couple_brackets(starting_string):
		return False

	for x in starting_string:
		if x not in brackets:
			starting_string = starting_string.replace(x,"")
	return starting_string


def check_right_of_brackets(starting_string:str) -> bool:
	'''check that brackets positioned correctly'''
	if not remove_characters(starting_string):
		return False
		
	string_without_letters = remove_characters(starting_string)
	couple_brackets = ['()','{}','<>','[]']

	while len(string_without_letters) > 0:
		startLen = len(string_without_letters)
		for x in couple_brackets:
			if x in string_without_letters:
				string_without_letters = string_without_letters.replace(x, "")
			if len(string_without_letters) == 0:
				return True
		if startLen == len(string_without_letters):
			break
	return False



print(check_right_of_brackets(input_string()))
