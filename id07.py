# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 11:33:47 2011

@author: steven
"""

# project euler problem ID 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10001st prime number?

primes = []
n = 2

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while len(primes) != 10001:
    if is_prime(n):
        primes.append(n)
    n += 1
   
print max(primes)
