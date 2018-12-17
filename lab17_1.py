#!/usr/bin/env python3
import cProfile
import math

def pow1(num):
	return num**2

def pow2(num):
	return pow(num,2)


def pow3(num):
	return math.pow(num,2)

def main():
	pow1(5)
	pow2(5)
	pow3(5)

main()


cProfile.run('main()')