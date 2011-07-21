# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:59:48 2011

@author: steven
"""

# project euler problem ID 48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def last10():
    i = 1
    total = 0
    while i <= 1000:
        total += i**i
        i += 1
    total = str(total)
    return total[-10:]
    
print last10()