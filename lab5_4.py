#!/usr/bin/python3

import math
import cmath

print('Enter a,b,c')

a = int(input())
b = int(input())
c = int(input())

discriminant = b**2-4*a*c

try:
    discr_sqrt=math.sqrt(discriminant)
except:
    discr_sqrt=cmath.sqrt(discriminant)

try:
    if discriminant < 0:
        x1=complex((-b+discr_sqrt)/(2*a))
        x2=complex((-b-discr_sqrt)/(2*a))
        print('X1 = ',x1) 
        print('X2 = ',x2)
    elif discriminant == 0:
	    x1 = -b / (2*a)
	    x2 = -b / (2*a)
	    print('x1 = ' + str(x1) + ' ,x2 = ' + str(x2))
    elif discriminant > 0:
	    x1 = (-b - discr_sqrt) / (2*a)
	    x2 = (-b + discr_sqrt) / (2*a)
	    print('x1 = ' + str(x1) + ' ,x2 = ' + str(x2))
except ZeroDivisionError:
	print('Error you can`t division on 0')