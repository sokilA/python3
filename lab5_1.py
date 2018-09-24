#!/usr/bin/python


x = int(input())

answer = int(x & (x - 1))
if answer == 0:
	print('True')
else:
    print('False')
