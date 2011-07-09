# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:46:42 2011

@author: steven
"""

# project euler problem ID 4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91  99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_pal(n):
    n = str(n)
    return n == n[::-1]
    
def generate():
    results = []
    for i in range(100, 1000):
        x = 100
        while x < 1000:
            if is_pal(i * x):
                results.append(i * x)
            x += 1
    return results

print max(generate())