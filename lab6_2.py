#!/usr/bin/env python3

def inputValue() -> list:
	summ, percent, years =  map(float, input('Enter your summ deposit, percent, years: ').split())
	return [summ, percent, years]

def calculationOfIncome(a:list) -> float:
	summ, percent, years = a
	i = 1
	while i <= years:
		i += 1;
		yearPercent = summ*(percent/100)
		summ += yearPercent
	return summ
	
print(calculationOfIncome(inputValue()))