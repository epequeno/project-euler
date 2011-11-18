# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 08:44:14 2011

@author: steven
"""

# project euler problem ID 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

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
   return sum(results)

print total()

# real    0m0.618s
# user    0m0.608s
# sys     0m0.016s

# method 2:
#def is_pal(n):
#   n = str(n)
#   return n == n[::-1]
#
#def is_pal_bin(n):
#   n = n[2:]
#   return n == n[::-1]
#
#def total():
#   i = 0
#   results = []
#   for i in range(1, 1000001):
#       if is_pal(i) and is_pal_bin(bin(i)):
#           results.append(i)
#   return sum(results)
#
#print total()

#real    0m0.473s
#user    0m0.460s
#sys     0m0.012s
