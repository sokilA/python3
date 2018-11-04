#!/usr/bin/env python3

def input_data() -> str:
	#input number
	start_string = (input('enter float number - '))
	return start_string


def convert_float_into_string(number:str):
	#function convert float number into string format
	one_dict = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',6:'six',7:'seven',8:'eight',9:'nine', 10: 'ten', 11:'eleven', 12:'twelf',
	 13:'thirteen', 14:'fourteen',15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eightteen', 19:'nineteen'}
	ten_dict = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty',6:'sixty',7:'seventy',8:'eighty'}
	top_number = {1:'hundred', 2:'thousand'}
	convert_string = ''
	dol,coin = number.split('.')
	zero = len(dol) - 1
	dol = int(dol)

	if dol >= 1000000: 
		return 'that function does not support number over million'

	num_for_division = int('1'+'0'*zero)

	
	while num_for_division >= 1:
		curent_num = int((dol/num_for_division)%10)

		if (num_for_division == 10 or num_for_division == 10000) and curent_num == 1:
			num_for_division /= 10
			curent_num = int(((dol/num_for_division)%10)+10)


		if num_for_division == 100000:
			convert_string += one_dict[curent_num] + ' hundred '
		if num_for_division == 10000:
			convert_string += ten_dict[curent_num] + ' '
		if num_for_division == 1000:
			convert_string += one_dict[curent_num] + ' thousand '
		if num_for_division == 100:
			convert_string += one_dict[curent_num] + ' hundred and '
		if num_for_division == 10:
			convert_string += ten_dict[curent_num] + ' '
		if num_for_division == 1:
			convert_string += one_dict[curent_num]

		num_for_division /= 10 

	convert_string += ' dollars and ' + coin + ' penny!'

	return convert_string



print(convert_float_into_string(input_data()))
