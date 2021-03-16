#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:21:55 2019

@author: fmalgarini
"""

def isprime(i):
	for cont in range(2, i):
		if (i%cont) == 0:
			return False
	return True

def prod(factors):
	product = 1
	for factor in factors:
		product = product*factor

	return product

def main():

	large_num = 600851475143
	factors = []

	for i in range(1, int(large_num/2)):
		if large_num % i == 0:
			if isprime(i):
				factors.append(i)
			
		if prod(factors) == large_num:
			break

	print(factors[-1:])

if __name__ == '__main__':
	main()
