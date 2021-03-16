#!/usr/bin/env python3

s, s_squared = 0, 0

for i in range(1,101):
	s += i 
	s_squared += i**2

s = s**2
print(s - s_squared)