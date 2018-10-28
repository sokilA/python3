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
	count = int(step)
	i = 1
	while len(mas_human) > 1:
		if i % count == 0:
			mas_human.pop(0)
		else:
			 next_el = mas_human.pop(0)
			 mas_human.append(next_el)
		i += 1

	
	return mas_human[0]



print(check_who_will_last(input_number()))