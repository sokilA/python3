#!/usr/bin/env python3
import math

print('Введіть значення a')
num_a = float(input())
print('Введіть значення b')
num_b = float(input())

x = (math.sqrt(num_a*num_b) / (math.e**num_a * num_b)) + num_a*math.e**((2*num_a) / num_b)

print('x = {0}'.format(x))