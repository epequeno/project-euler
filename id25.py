# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:41:12 2011

@author: steven
"""

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def test():
    i = 0
    while len(str(fibo(i))) != 1000:
        i += 1
        fibo(i)
    return i
    
print test()