#!/usr/bin/env python3
import math

def inputValue() -> list:
	firstSide, secondSide, thirdSide = map(float, input('Enter 3 side of triangle: ').split())
	return [firstSide, secondSide, thirdSide]

def isTriangleExist(a:list) -> bool:
	if (((a[0] + a[1]) > a[2]) and ((a[0] + a[2]) > a[1]) and ((a[2] + a[1] > a[0]))):
		return True
	else:
		return False


def areaOfTriangle(a:list) -> float:
	if isTriangleExist(a):
		p = (a[0]+a[1]+a[2])/2
		area = math.sqrt(p*(p-a[0])*(p-a[1])*(p-a[2]))
		return area
	else: 
		return 'Triangle not exists'

print(areaOfTriangle(inputValue()))