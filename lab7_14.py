#!/usr/bin/env python3 
import re

def input_email() -> str:
	''' Enter email '''
	email = input('Enter your email: ')
	return email


def check_correctness_of_email(email:str) -> str:
	is_valid = re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$", email)
	if is_valid:
		return 'your email is correct'
	else:
		return 'your email is not correct'

print(check_correctness_of_email(input_email()))