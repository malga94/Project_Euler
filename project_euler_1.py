#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:21:55 2019

@author: fmalgarini
"""
cont = 0

for i in range(1, 1000):
	if i%3 == 0 or i%5 == 0:
		cont += i

print(cont)