#!/usr/bin/python3

first_side = int(input('Enter first side for triangel'))
second_side = int(input('Enter second side for triangel'))
third_side = int(input('Enter third side for triangel'))

if first_side+second_side > third_side:
	print('can exist')
elif first_side+third_side > second_side:
	print('can exist')
elif second_side+third_side > first_side:
	print('can exist')
else:
	print('can`t exist')