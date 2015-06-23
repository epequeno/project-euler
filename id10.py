# -*- coding: utf-8 -*-
"""
Created on Tue Jun  23 03:05:47 2015

@author: steven
"""

# project euler problem ID 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# from http://stackoverflow.com/a/19346310
def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps

print sum(primes(2000000))
