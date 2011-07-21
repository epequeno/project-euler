# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 21:41:09 2011

@author: steven
"""

# project euler problem ID 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def primeFactors(n, factor):
    factors = []
    while (n % factor != 0):
        factor += 1

    factors.append(factor)

    if n > factor:
        factors.extend(primeFactors(n / factor, factor))

    return factors

print primeFactors(600851475143, 2)