#!/usr/bin/env python3

def input_data() -> list:
	#input starting string
	start_string = (input('enter your string - '))
	return start_string

def convert_string_into_morze(string:str)-> str:
	#convert text into morze format
	dict_morze = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.",
	"G":"--.","H":"....","I":"..","J":"-.-.","K":"-.-","L":".-..","M":"--",
	"N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
	"U":"..-","V":"...-","W":".--","X":".-..","Y":"-.--","Z":"--.."}

	morze_string = ''.join([dict_morze.get(i.upper(), ' ') for i in string])

	return morze_string

print(convert_string_into_morze(input_data()))