#!/usr/bin/env python3

import math

def isprime(i):
	top_val = int(math.ceil(math.sqrt(i)))

	for x in range(2, top_val+1):
		
		if i%x == 0:
			return False

	return True

def main():
	n = 1
	i = 3
	
	positionOfPrime = 10001
	while n < positionOfPrime:
		if isprime(i):
			n += 1
			
		i += 1

	print(i-1)

if __name__ == '__main__':
	main()

