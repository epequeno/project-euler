# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:51:47 2011

@author: steven
"""

def total():
   number = str(2**1000)
   total = 0
   for i in number:
       total += int(i)
   return total

print total()