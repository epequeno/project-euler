# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:07:14 2011

@author: steven
"""

# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
# contain the same digits.

def find_that_number():
    x = 2
    matches = 0
    while matches != 5:
        for multiplier in range(2, 7):
            if sorted(str(x)) == sorted(str(x * multiplier)):
                matches += 1
        if matches == 5:
            print x
        else:
            x += 1
            matches = 0
    
find_that_number()

# real	0m2.039s
# user	0m2.036s
# sys	0m0.000s