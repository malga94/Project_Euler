# -*- coding: utf-8 -*-
"""
Project Euler problem 108 solution

Problem statement: https://projecteuler.net/problem=108

@author: fmalgarini
"""
requested_sol = 300

solutions, n = 0, 1000
while solutions < requested_sol:
    solutions = 2
    y = n**2
    for x in range(2, n):
        if y%x == 0:
            solutions += 1
        if n - x < requested_sol - solutions:
            break

    #print(n, solutions)
    n += 1

print(n-1)
