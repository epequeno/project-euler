# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 22:56:55 2011

@author: steven
"""

# project euler problem ID 6
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025  385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sum_sq():
    total = 0
    for i in range(1, 101):
        total += i**2
    return total
    
def sq_sum():
    total = 0
    for i in range(1, 101):
        total += i
    return total**2

def diff():
    return sq_sum() - sum_sq()

print diff()

# real    0m0.009s
# user    0m0.000s
# sys     0m0.008s