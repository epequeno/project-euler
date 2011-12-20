# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 21:24:20 2011

@author: steven
"""

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20? 232792560

"""
def is_div(n):
    a = []
    for i in range(1, 21):
        a.append(n % i)
    return a.count(0)
    
def count():
    seed = 1
    while is_div(seed) != 20:
#        print seed, is_div(seed)
        seed += 1
        is_div(seed)
    return seed
"""

# real    32m2.097s
# user    31m41.095s
# sys     0m17.069s

#Version 2:

def is_div(n):
    i = 2
    while i < 21:
        if n % i != 0:
            return False
        else:
            i += 1
    return True

def test():
    init = 2520
    while is_div(init) != True:
        init += 1
    return init

print test()


#real    1m54.848s
#user    1m54.723s
#sys	 0m0.044s



