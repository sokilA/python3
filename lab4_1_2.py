#!/usr/bin/env python3
import math

print('Введіть значення a')
num_a = float(input())
print('Введіть значення b')
num_b = float(input())
print('Введіть значення c')
num_c = float(input())

x = (1 / (num_c*math.sqrt(2*math.pi)))*math.exp(-(((num_a-num_b)**2)/(2*num_c**2)))

print('x = {0}'.format(x))