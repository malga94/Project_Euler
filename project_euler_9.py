#!/usr/bin/env python3

for c in range(334,1000):
	for b in range(0, c):
		for a in range(0, b):
			if a + b + c == 1000:
				if a**2 + b**2 == c**2:
					print(a,b,c)
					print("Product: {0}".format(a*b*c))
					exit()

