# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 21:24:20 2011

@author: steven
"""

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20? 232792560

def is_div(n):
    a = []
    for i in range(1, 21):
        a.append(n % i)
    return a.count(0)
    
def count():
    seed = 1
    while is_div(seed) != 20:
#        print seed, is_div(seed)
        seed += 1
        is_div(seed)
    return seed

print count()