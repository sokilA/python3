#!/usr/bin/env python3

def inputValue() -> float:
	summ, expectedSumm, percent =  map(float, input('Enter your summ deposit, expected summ, percents: ').split())
	return [summ, expectedSumm, percent]

def calculationHowMuchNeedYears(a:list) -> float:
	summ, expectedSumm, percent = a
	year = 0
	while summ <= expectedSumm:
		summ = summ + (summ*(percent/100))
		year += 1
	return year
	
print(calculationHowMuchNeedYears(inputValue()))