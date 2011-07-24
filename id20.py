# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:10:29 2011

@author: steven
"""

# project euler problem ID 20
# n! means n x (n - 1) x ... x 3 x 2 x 1
#
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import math

def fac():
    number = str(math.factorial(100))
    total = 0
    for i in number:
        total += int(i)
    return total

print fac()

# real    0m0.010s
# user    0m0.012s
# sys     0m0.000s