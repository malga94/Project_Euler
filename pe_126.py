# -*- coding: utf-8 -*-
"""
Project Euler problem 126 solution

Problem statement: https://projecteuler.net/problem=126

@author: fmalgarini
"""

import math
from mod.modules import triang_numbers

def calc_layer(i,j,k,n):

    #Formula for the number of cubes on the n-th layer (starting from n=1)
    layer = 2*(i*j+i*k+j*k) + 4*(n-1)*(i+j+k) + triang_numbers(n-2)*8
    return layer

def extract_max(Cofn):

    val = 1000
    indexes = []
    for key in Cofn.keys():
        if Cofn[key] == val:
            indexes.append(key)

    indexes.sort()
    return indexes

def main():

    #Chose max_size knowing the correct answer, previously was 30000 when I found it
    max_size = 20000
    cofn = {}
    #Number of cubes in a layer always even
    for x in range(2, max_size, 2):
        cofn[x] = 0

    #Since the first layer has already 2*(i*j + i*k + j*k) cubes, even assuming i=j=1 we can use
    #k < max_size/2 if we are only interested in layers with less than max_size cubes
    #Similarly, since i<j<k, we can write j < sqrt(max_size/2), which happens when i=1 and j=k
    #In principle i can only be < cuberoot(max_size/2), which gives negligible time improvement
    for i in range(1, math.ceil(math.sqrt(max_size/2))):
        for j in range(1, math.ceil(math.sqrt(max_size/2))):
            for k in range(1, int(max_size/2)+1):
                if i<=j and j<=k and i*j + i*k + j*k <= max_size:
                    n=1

                    layer = 0
                    while layer <= max_size:
                        layer = calc_layer(i, j, k, n)
                        n+=1
                        try:
                            cofn[layer] += 1
                        except KeyError:
                            continue
                        except Exception as e:
                            print(str(e))
                            exit()


    indices = extract_max(cofn)
    print(min(indices))

if __name__ == '__main__':
    main()
