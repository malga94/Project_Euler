# -*- coding: utf-8 -*-
"""
Useful functions for Project Euler problems

@author: fmalgarini
"""
import math
import random

def is_prime(n):
    #Function to check if an integer n is prime

    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True

def euler_prime_test(n, cont):

    a = random.randint(2, n-1)
    x = pow(a, int((n-1)//2), n)
    
    if cont < 20:
        if x == 1 or x == n-1:
            cont += 1
            euler_prime_test(n, cont)

        else:
            return False

    return True

def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
