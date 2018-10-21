#!/usr/bin/env python3

def input_string(string:str) -> str:
	''' Enter start strings '''
	starting_string = input('Enter {} string:'.format(string))
	return starting_string

def count_letters(string_for_count:str) -> dict:
	''' counting letters '''
	dict_letters = {}
	for x in string_for_count:
		if x not in dict_letters:
			count = string_for_count.count(x)
			dict_letters.update({x:count})
	return dict_letters

def check_creating(dict_first_string:dict,dict_second_string:dict) -> str:
	''' if you can ctreate second string from first string function return "you can create"
	 otherwise the function return "you can`t create" '''
	for key, value in dict_second_string.items():
		if key not in dict_first_string:
			return 'you can`t create'
		elif value > dict_first_string[key]:
			return 'you can`t create'

	return 'you can create'


print(check_creating(count_letters(input_string('first')),count_letters(input_string('second'))))

