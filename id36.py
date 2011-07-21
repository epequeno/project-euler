# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 08:44:14 2011

@author: steven
"""

# id 36

def is_pal(n):
   n = str(n)
   return n == n[::-1]

def is_pal_bin(n):
   n = n[2:]
   return n == n[::-1]

def total():
   i = 0
   results = []
   while i < 1000000:
       if is_pal(i) and is_pal_bin(bin(i)):
           results.append(i)
       i += 1
   total = 0
   for x in results:
       total += x
   return total

print total()