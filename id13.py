# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 07:46:44 2011

@author: steven
"""

number = open('number.txt')

def total():
   total = 0
   for line in number:
       total += int(line)
   total = str(total)
   print total[:10]

total()