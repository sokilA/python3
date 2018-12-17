#!/usr/bin/env python3
import unittest
import math


def formula(num_a:int, num_b:int):
	if num_b == 0:
		return False
	return (math.sqrt(num_a*num_b) / (math.e**num_a * num_b)) + num_a*math.e**((2*num_a) / num_b)


	

class Testing(unittest.TestCase):

	def test_formula_1(self):
		self.assertEqual(formula(0,1), 0.0)

	def test_formula_2(self):
		self.assertAlmostEqual(formula(0.5,10), 0.688209837593, 12)

	@unittest.expectedFailure
	def test_fail(self):
		self.assertEqual(formula(1,0), 2)

	def test_formula_3(self):
		self.assertFalse(formula(1,0), False)
	


if __name__ == '__main__':
	unittest.main()