#!/usr/bin/env python3


def input_string() -> str:
	''' Enter start string '''
	starting_string = input('Enter your string: ')
	return starting_string

def the_shortest_word(string:str):
	# return the shortest word in string
	mas_words = sorted(string.split(), key=len)
	len_words = len(mas_words[0])
	mas_the_shortes_word = []
	for i in mas_words:
		if len_words == len(i):
			mas_the_shortes_word.append(i)
		else:
			break

	return ','.join(mas_the_shortes_word)

print('The shortest word is - ' + the_shortest_word(input_string()))