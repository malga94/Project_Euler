#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def isprime(x):

	for i in range(2, math.ceil(math.sqrt(x))+1):
		if x%i == 0:
			return False

	return True

def next_iteration(l):

	#Function that takes a list l of length N and returns a list x of length N-1 for which the difference between the n and n-1 element is given by the n_th element of 
	x = [1]
	for cont, val in enumerate(l[1:-1]):
		temp = x[cont]
		x.append(temp + val)
		
	return x

def squarefree(pascal, primes):

	#Function that returns true if the integer pascal is a squarefree number. This means that no square of a prime divides it
	for i in primes:
		if pascal%i == 0:
			return False

	return True

def main():

	n_th_triangnum = []
	l = []

	#Here the idea is to build the diagonals of the Pascal triangle with 51 lines: I start from the first non-constant diagonal (skipping the exterior one with only 1s), which is just the natural numbers up to 50
	for i in range(1,51):
		l.append(i)
	n_th_triangnum.append(l)
	#Then I call the function next_iteration, passing the previous diagonal (in this case the first 50 natural numbers): this function returns a list, shorter by one element, of the next order of triangular numbers
	x = next_iteration(l)
	n_th_triangnum.append(x)
	#Starting from triangular numbers, I construct the next order sequence (tetrahedral numbers), and then the next and so on recursively until I have all 50 diagonals of the Pascal triangle
	for var in range(2,50):
		x = next_iteration(x)
		n_th_triangnum.append(x)

	#Unpack the list of lists
	pascal_values = []
	for inner_list in n_th_triangnum:
		for elem in inner_list:
			pascal_values.append(elem)

	#We are only interested in unique values: remove repeated elements and sort
	pascal_values = list(set(pascal_values))
	pascal_values.sort()

	#Build a list of squares of primes
	square_prime_list = [4]
	for i in range(2, math.ceil(pascal_values[-1]**0.25)):
		if isprime(i):
			square_prime_list.append(i*i)

	#Check if pascal element is squarefree; if yes, put it in list
	squarefree_pascal_values = []
	for pascal in pascal_values:
		if squarefree(pascal, square_prime_list):
			squarefree_pascal_values.append(pascal)

	#Finally, sum all elements of said list, and get the answer to problem 203
	pascal_sum = 0
	for e in squarefree_pascal_values:
		pascal_sum += e

	print(pascal_sum)

if __name__ == "__main__":
	main()