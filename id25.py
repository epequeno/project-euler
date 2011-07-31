# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:41:12 2011

@author: steven
"""

# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = F(n - 1) + F(n - 2), where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

known = {0:0, 1:1}

def fibo(n):
    if n in known:
        return known[n]
    else:
        res = fibo(n - 1) + fibo(n - 2)
    known[n] = res
    return res

def test():
    i = 0
    while len(str(fibo(i))) < 1000:
        i += 1
        fibo(i)
    return i, len(str(fibo(i))), fibo(i)
    
print test()

#real	0m0.474s
#user	0m0.464s
#sys	0m0.012s