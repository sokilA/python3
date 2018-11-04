#!/usr/bin/env python3
import collections

def input_number() -> int:
	"""input simple number"""
	number = input('Enter your number: ')
	return number

def input_roman_number() -> str:
	"""input roman number"""
	roman_number = input('Enter your rome number: ')
	return roman_number

def from_num_to_rom(number:int) -> str:
	#function replace simple numbers into roman numbers
	roman_replace_dict = collections.OrderedDict([('I'*5, 'V'), ('V'*2,'X'), ('X'*5,'L'), ('L'*2,'C'),('C'*5,'D'),
	('D'*2,'M'),('DCCCC','CM'),('CCCC','CD'),('LXXXX','XC'),('XXXX','XL'),('VIIII','IX'),('IIII','IV')])
	roman_convert = 'I'*int(number)
	for key, val in roman_replace_dict.items():
		roman_convert = roman_convert.replace(key,val)
	return roman_convert

def from_rom_to_num(string:str) -> str:
	#function replace roman numbers into simple numbers
	numbers_according_to_roman = collections.OrderedDict([('CM','900 '),('CD','400 '),('XC','90 '),('XL','40 '),('IX','9 '),('IV','4 '),
	('I', '1 '),('V','5 '),('X','10 '),('L','50 '),('C','100 '),('D','500 '),('M','1000 ')])
	number_convert = string
	for key, val in numbers_according_to_roman.items():
		number_convert = number_convert.replace(key, val)

	number_convert = number_convert.strip()
	result = number_convert.split(' ')
	result = list(map(int, result))
	result = sum(result)

	return result



print(from_num_to_rom(input_number()))
print(from_rom_to_num(input_roman_number()))
