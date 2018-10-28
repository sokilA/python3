#!/usr/bin/env python3

def input_number() -> list:
	''' Enter start string '''
	number = []
	number.append(input('Enter number of human: '))
	number.append(input('Enter step: '))
	return number


def check_who_will_last(date:list) -> int:
	number, step = date
	mas_human = [i for i in range(1,int(number)+1)]
	count = int(step) - 1 
	for i in range(0,len(mas_human)):
		if len(mas_human) == 1:
			break
		print(count)
		mas_human.pop(count)
		print(mas_human)
		count += int(step) - 1 
		j = 0
		while count >= len(mas_human):
			count = count - len(mas_human)

	
	return mas_human[0]



print(check_who_will_last(input_number()))



