# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 22:56:55 2011

@author: steven
"""

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