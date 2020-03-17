# -*- coding: utf-8 -*-
"""
Project Euler problem 146 solution

Problem statement: https://projecteuler.net/problem=146

@author: fmalgarini
"""
from mod.modules import is_prime, euler_prime_test, miller_rabin
import math

vals_to_sum = [1,3,7,9,13,27]

def check_primality(n, flag):
    """Checking primality of n^2+x, with x in vals_to_sum. Using 3 different functions to check
    is_prime is extremely slow; the other two are implementations of the Euler test and the Miller-Rabin test
    (the Miller-Rabin was taken from https://gist.github.com/Ayrx/5884790, will write my own implementation later)"""
    for i in vals_to_sum:
        if flag == 0:
            if miller_rabin(n**2 + i, 40) == False:
                return False
        elif flag == 1:
            if is_prime(n**2 + i) == False:
                return False
        elif flag == 2:
            if euler_prime_test(n**2 + i, 0) == False:
                return False
    #Since n^2+x (x in vals_to_sum) must be CONSECUTIVE primes, we have to check that n^2+19 and n^2+21 are not prime
    #(all the other odd values between n^2+13 and n^2+27 are trivially not prime)
    for i in [19, 21]:
        if flag == 0:
            if miller_rabin(n**2 + i, 40) == True:
                return False
        elif flag == 1:
            if is_prime(n**2 + i) == True:
                return False
        elif flag == 2:
            if euler_prime_test(n**2 + i, 0) == True:
                return False

    return True

def main():

    max = 150*10**6
    """Notice that only multiples of 10 can satisfy the problem statement. Infact, n^2+1, n^2+2, n^2+3 and n^2+4 all
    cannot be divisible by 5, else n^2+1, n^2+7, n^2+3 and n^2+9 wouldn't be prime respectively, contradicting the
    problem statement. So n^2 and n^2+5 are divisible by 5. But n^2 must of course be even, so it is divisible also
    by 2, and therefore by 10. But if n^2 is divisible by 10, so is n: hence the step of 10 in the list 'integers'"""

    integers = list(range(10, max, 10))
    integers_reduced = [x for x in integers if (x**2 - 100) % 210 == 0 and x%13 != 0]

    solutions = []
    cont = 0

    for n in integers_reduced:
        if cont%100 == 0:
            print("Working on n={0}".format(n))
        if check_primality(n, 2) == True:
            solutions.append(n)
        cont += 1

    x = 0
    print(solutions)
    for num in solutions:
        x += num

    print("The sum of n below 150 million is ", x)

if __name__ == '__main__':
    main()
