#!/usr/bin/env python3
import math

def divisors(i):
	var = 0
	
	maxval = int(math.sqrt(i)) + 1
	for k in range(2, maxval):
		if i%k == 0:
			
			var += 1

	#1 and the number itself count as divisors. Eg for 15 we have var=2, because the code finds 3,5. But we also want to count 1 and 15
	return var*2 + 2

i = 1
cont = 2
div = 0
while not div > 500:
	i += cont
	cont += 1
	div = divisors(i)

print(i)
