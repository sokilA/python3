#!/usr/bin/env python3

print('Введіть вашу вагу')
mas = input()
print('Введіть ваш зріст')
height = input()

bmi = int(mas) / float(height) ** 2

print('Ваш BMI: {0}'.format(bmi))