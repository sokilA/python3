#!/usr/bin/env python3
import math

def input_number_of_ticket() -> str:
	''' Enter start strings '''
	tickets_number = input('Enter number of your tickets:')
	return tickets_number

def check_lucky_ticket(number:str) -> bool:
	#function return true if ticket is lucky or false if is`t
	mas_number = list(number)
	center_of_mas = math.floor(len(mas_number)/2)
	left_sum = 0
	right_sum = 0

	for i in range(0,center_of_mas):
		left_sum += int(mas_number[i])
		right_sum += int(mas_number[-(i+1)])

	if left_sum == right_sum:
		return True
	else:
		return False

print(check_lucky_ticket(input_number_of_ticket()))