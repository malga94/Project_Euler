# -*- coding: utf-8 -*-
"""
Project Euler problem 65 solution

Problem statement: https://projecteuler.net/problem=65

@author: fmalgarini
"""

from fractions import Fraction

generating_list = [1]
#Generating the continued fraction expansion for e, [1,2,1,1,4,1,1,6...]
for i in range(0, 99):
    if i%3 == 0:
        generating_list.append(int(2 * (i/3 + 1)))
    else:
        generating_list.append(1)

cont = -1
init_val = 2 #The first term in the continued fraction expansion

def cont_frac(generator):
    global cont
    cont += 1
    global init_val
    if cont == 0:
        val = Fraction(init_val + 1 / cont_frac(generating_list[cont]))

    elif cont < len(generating_list)-1:
        #recursive function calls itself with next value in the generating list
        val = Fraction(generator + 1 / cont_frac(generating_list[cont]))

    else:
        #for the last iteration, it simply returns the last value of the generating list
        return generating_list[cont]

    return val

def sum_of_digits(num):

    #simple function implementing digit sum
    sum = 0
    while num:
        sum += num % 10
        num = num // 10

    return sum

def main():

    val = cont_frac(generating_list[0])

    digitsum = sum_of_digits(val.numerator)
    print(digitsum)

if __name__ == '__main__':
    main()
