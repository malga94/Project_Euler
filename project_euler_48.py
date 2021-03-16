#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:40:22 2019

@author: fmalgarini

Solution to Problem 48 of Project Euler
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

x = 0
for i in range(1,1001):
	x += i**i

print(str(x)[-10:])