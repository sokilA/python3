#!/usr/bin/env python3

print('Введіть градуси Фаренгейта')
temperature_Fahrenheit = input()

temperature_Celsius = (int(temperature_Farengate) - 32) / 1.8

print('{0} градусів Фаренгейта відповідає: {1} градусам Цельсія'.format(temperature_Fahrenheit, temperature_Celsius))
