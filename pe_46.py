# -*- coding: utf-8 -*-
"""
Project Euler problem 46 solution

Problem statement: https://projecteuler.net/problem=46

@author: fmalgarini
"""
import math
from mod.modules import is_prime

def check_goldbach(prime_list, x):
    #Function to check if an odd composite integer x satisfies i + 2*j^2 = x, where i is a prime number and j is an integer

    for i in prime_list:
        for j in range(1, math.floor(math.sqrt(x))):
            if i + 2*j**2 == x:

                return True

    return False

def main():

    max = 10000
    prime_list = [1,2]
    for n in range(3, max):
        if is_prime(n) == True:
            prime_list.append(n)

    #Generating a list of odd composite numbers by difference between a list of all odd numbers from 1 to max and the list of primes from 1 to max
    composite_list = list(set(list(range(1, max, 2))) - set(prime_list))

    for composite in composite_list:
        #We only need to check the Goldbach conjecture for primes smaller than our composite number
        primes = [x for x in prime_list if x < composite]

        if check_goldbach(primes, composite) == False:
            print("The first number that does not satisfy Goldbach's conjecture is {0}".format(composite))
            exit()

    print("No number has been found")

if __name__ == '__main__':
    main()
