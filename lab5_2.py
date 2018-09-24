#!/usr/bin/python3

print('Enter height and width your door')

height = int(input()) 
width = int(input()) 

print('Enter size of box')

box_height = int(input()) 
box_width = int(input()) 
box_length = int(input()) 

if height > box_height and width > box_width:
	print('The box fit for that door')
elif height > box_width and width > box_height:
	print('The box fit for that door')
elif height > box_height and width > box_length:
	print('The box fit for that door')
elif height > box_width and width > box_length:
	print('The box fit for that door')
else:
	print('The box doesn`t fit for that door')
