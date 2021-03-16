#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:40:22 2019

@author: fmalgarini

Solution to Problem 13 of Project Euler
Text of the problem:

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""

k_constant = ""
for d in range(1, 1000001):
	k_constant += str(d)

result = int(k_constant[0]) * int(k_constant[9]) * int(k_constant[99]) * int(k_constant[999]) * int(k_constant[9999]) * int(k_constant[99999]) * int(k_constant[999999])
print(result)