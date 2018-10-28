#!/usr/bin/env python3
from statistics import median

def list_of_number() -> list:
	number = input('Enter range of list: ')
	number_list = [i for i in range(1,int(number)+1)]
	return number_list


def mediana_and_mid(number_list:list) -> list:
	date = []
	date.append(median(number_list))
	date.append(float(sum(number_list)) / len(number_list))
	return date



date = mediana_and_mid(list_of_number())

print('mediana - {0} average value - {1}'.format(date[0],date[1]))


