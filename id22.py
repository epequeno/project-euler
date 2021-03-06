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

# real    0m0.045s
# user    0m0.036s
# sys     0m0.008s

# Method 2:
    
#def alphabetize():
#   ordered = []
#   for item in names:
#       ordered.append(item.strip('"'))
#   ordered.sort()
#   return ordered
#
#names = alphabetize()
#
#def name_score(name):
#    total = 0
#    for letter in name:
#        total += (ord(letter) - 64)
#    return total
#    
#def position_score(name):
#    return names.index(name) + 1
#    
#def summation():
#    names = alphabetize()
#    total = 0
#    for name in names:
#        total += (name_score(name) * position_score(name))
#    return total
#
#print summation()

#real   0m0.282s
#user	0m0.276s
#sys	0m0.004s