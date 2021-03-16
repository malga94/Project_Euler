#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:21:55 2019

@author: fmalgarini
"""

import math

def ispalindrome(num):
	num_girato = []
	num_normale = num
	digits = int(math.log10(num))+1

	for i in range(0, digits):
		num_girato.append(num%10)
		num = num//10
	
	temp = [str(i) for i in num_girato]
	num_girato_intero = int("".join(temp))

	if num_normale == num_girato_intero:
		return True

	return False

def main():

	palindromi = []
	for i in range(100, 1000):
		for j in range(100, 1000):
			if ispalindrome(i*j):
				palindromi.append(i*j)

	palindromi.sort()
	print(palindromi[-1:])

if __name__ == '__main__':
	main()