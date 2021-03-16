#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:40:22 2019

@author: fmalgarini

Solution to Problem 13 of Project Euler
Text of the problem:

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

"""

import pandas as pd

sum = 0
df = pd.read_csv('large_sum.csv', header=None)

for column in df:
	sum += int(df[column])

print(str(sum)[:10])


