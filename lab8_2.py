#!/usr/bin/env python3
import random

def list_of_number() -> list:
	number = input('Enter range of list: ')
	number_list = [i for i in range(1,int(number)+1)]
	random.shuffle(number_list)
	return number_list


def quicksort(nums):
	if len(nums) <= 1:
		return nums
	else:
		q = random.choice(nums)
		l_nums = [n for n in nums if n < q]

	e_nums = [q] * nums.count(q)
	b_nums = [n for n in nums if n > q]
	return quicksort(l_nums) + e_nums + quicksort(b_nums)


mas = list_of_number()
print('primary array - {0}'.format(mas))
print('after quicksort - {0}'.format(quicksort(mas)))