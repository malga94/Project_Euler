#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 6 23:23:30 2020

@author: fmalgarini
"""

from operator import add, sub, mul, truediv
from itertools import product, permutations, combinations

operations = {'+':add, '-':sub, '*':mul, '/':truediv}

def generate_ps():
	#Generate all possible sets of 4 digits satisfying a<b<c<d
	possible_set_list = []
	s = ''
	all_comb = combinations('0123456789', 4)
	for value in all_comb:
		s = ''
		for i in range(4):
			s += str(value[i])
		possible_set_list.append(s)
	
	return possible_set_list

def do_operations(i, a,b,c,d, select):
	#Perform the set of operations i (a tuple with 3 operators, to be placed between each pair of integers) on the 4 integers a,b,c,d. Returns the result, stored in res
	#The integer select chooses between one of four possible order of operations, which exhaustes all the possible order of operations one can have by using parentheses
	try:
		if select == 0:
			#First order of operations
			temp = operations.get(i[0])(a,b)
			temp2 = operations.get(i[2])(c,d)
			res = operations.get(i[1])(temp, temp2)

		elif select == 1:
			#Second order of operations
			temp = operations.get(i[0])(a,b)
			temp2 = operations.get(i[1])(temp,c)
			res = operations.get(i[2])(temp2,d)

		elif select == 2:
			#Third order of operations
			temp = operations.get(i[1])(b,c)
			temp2 = operations.get(i[0])(a,temp)
			res = operations.get(i[2])(temp2,d)

		elif select == 3:
			#Fourth order of operations
			temp = operations.get(i[2])(c,d)
			temp2 = operations.get(i[1])(b,temp)
			res = operations.get(i[0])(a,temp2)
		return res

	except ZeroDivisionError:
		return -1

def	get_num_consecutive_vals(clean_results):
	#Returns the number of consecutive integer values in the list, starting from 1. If the list starts with anything but 1, it returns the first element. If the whole list is natural numbers up to len(list), it returns the last element of the list
	cont = 1
	for val in clean_results:
		if val != cont:
			if cont > 1:
				return clean_results[cont-2]
			else:
				return clean_results[0]
		cont += 1

	return val

def main():

	num_consecutive_vals = []
	possible_sets = generate_ps()
	for a in possible_sets:
		results = []
		#Generate all possible orders of the 4 digits a,b,c,d
		abcd = permutations(a, 4)
		for x in abcd:
			a,b,c,d = int(x[0]), int(x[1]), int(x[2]), int(x[3])
			
			#Generate all possible orders (with repetition) of the operations +,-,*,/ appearing 3 times
			symbols = product('+-*/', repeat=3)
			for i in symbols:
				
				for select in range(4):
					results.append([a,b,c,d,i,select,do_operations(i, a,b,c,d, select)])

		#We are not interested in negative numbers, or non-integers: let's remove them and store the remaining, natural numbers into a new list
		clean_results = []
		for r in results:
			if r[6]%1 == 0 and r[6] > 0:
				clean_results.append(r[6])

		#We don't want results of the operations appearing twice, since we are only interested in what results we can obtain with the digits a,b,c,d and the operations i
		clean_results = list(set(clean_results))
		clean_results.sort()
		numvals = get_num_consecutive_vals(clean_results)
		num_consecutive_vals.append(numvals)

	#Get the index corresponding to the highest number of consecutive values, and obtain the corresponding values of the integers a,b,c,d
	max_index = num_consecutive_vals.index(max(num_consecutive_vals))
	print(possible_sets[max_index])

if __name__ == '__main__':
	main()