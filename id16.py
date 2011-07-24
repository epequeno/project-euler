# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:51:47 2011

@author: steven
"""

# project euler problem ID 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def total():
   number = str(2**1000)
   total = 0
   for i in number:
       total += int(i)
   return total

print total()

# real    0m0.010s
# user    0m0.016s
# sys     0m0.000s