# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:10:29 2011

@author: steven
"""

import math

def fac():
    number = str(math.factorial(100))
    total = 0
    for i in number:
        total += int(i)
    return total

print fac()