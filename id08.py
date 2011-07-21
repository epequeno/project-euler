# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:52:01 2011

@author: steven
"""
number = open('number2.txt')
number = str(number.read())

def product():
    candidates = []
    i = 0
    while i < (len(number) - 5):
        group = number[i:i + 5]
        total = 1
        for digit in group:
            total *= int(digit)
        candidates.append(total)
        i += 1
    return max(candidates)

print product()