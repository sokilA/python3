#!/usr/bin/env python3

def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string

def add_frame(string:str) -> str:
	''' add frame for any string'''
	top_bot_frame = '*****************'
	center_frame = '*  {}  *'.format(string)
	return '{0}\n{1}\n{2}'.format(top_bot_frame,center_frame,top_bot_frame)

print(add_frame(input_string()))