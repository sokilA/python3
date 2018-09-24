#!/usr/bin/python3


num = int(input('Enter number for cheking - '))

def is_simple(x):
    n = 2
    if x < n:
        return False
    else:    
        while n < x:
            if x % n == 0:
                return False
                break
            n = n + 1
        else:
            return True

state = is_simple(num)
 
if state:
	print('Your number is simple')
else:
	print('Your number is not simple')