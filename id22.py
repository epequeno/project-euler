# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 08:41:14 2011

@author: steven
"""
names = open('names.txt')
names = names.read()
names = names.split(",")

def alpha():
   alpha = []
   for i in names:
       alpha.append(i.strip('"'))
   alpha.sort()
   return alpha

def count():
   i = 1
   totals = []
   answer = 0
   for name in alpha():
       score = []
       for letter in name:
           score.append(ord(letter) - 64)
           total = 0
           for item in score:
               total += item
       totals.append(total * i)
#        print name, i, total
       i += 1
   for individual_score in totals:
       answer += individual_score
   print answer

count()