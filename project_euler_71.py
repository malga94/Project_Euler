#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:21:55 2019

@author: fmalgarini
"""

import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize) #Prints whole numpy array

M = 10
fractions = np.zeros((1000, 2))
i = 0

for n in range(1, M):
	for d in range(n+1, M+1):
		if (d%n != 0 or n==1):
			fractions[i,0] = n
			fractions[i,1] = d
			i += 1

print(fractions)