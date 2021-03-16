#!/usr/bin/env python3

import math 

def slow_sieve(max_num):

	top_val = int(math.ceil(math.sqrt(max_num)))
	primes = []
	for i in range(1, max_num):
		primes.append(i)

	lista = [2]
	for val in range(3, top_val, 2):
		lista.append(val)

	for x in lista:
		for y in primes:
			if y%x == 0 and y>x:
				primes.remove(y)
	primes.remove(1)
	return primes

def sieve(max_num):

	marked = [0]*max_num
	val = 3
	s = 2
	while val <= max_num:
		if marked[val] == 0:
			s+=val
		i = val**2

		while i < max_num:
			marked[i] = 1
			i += val
		val += 2

	return s

def isprime(i):
	top_val = int(math.ceil(math.sqrt(i)))

	for x in range(2, top_val+1):
		
		if i%x == 0:
			return False

	return True

def main():

	maxval = 1000000000
	# somma = 2
	# for i in range(3, maxval, 2):
	# 	if isprime(i):
	# 		somma += i

	#print(somma)
	# primes = slow_sieve(20000)
	# print(sum(primes))

	somma = sieve(maxval)
	print(somma)

if __name__ == '__main__':
	main()


