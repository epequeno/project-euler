# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 08:41:14 2011

@author: steven
"""

# project euler problem ID 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into 
# alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
# would obtain a score of 938  53 = 49714.
#
# What is the total of all the name scores in the file?

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