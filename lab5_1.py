#!/usr/bin/python3


num = int(input())

answer = int(num & (num - 1))
if answer == 0:
	print('True')
else:
    print('False')
