# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:15:37 2011

@author: steven
"""

# project euler problem ID 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def problem():
    total = 0
    for i in range(1, 1000):
        if ((i % 3) == 0) or ((i % 5) == 0):
            total += i
    return total

print problem()

# real    0m0.021s
# user    0m0.008s
# sys     0m0.012s