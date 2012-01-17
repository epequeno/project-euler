# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:57:04 2012

@author: steven
"""
# project euler ID14
# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following
# sequence:

# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

def apply_rule(x):
    if x == 1:
        return 1
    elif x % 2 == 0:
        return x / 2
    else:
        return (3 * x) + 1
        
        
def test(x):
    start = x
    results = []
    while start > 1:
        results.append(start)
        start = apply_rule(start)
    return results
    
def find_longest():
    results = []
    for i in range(1, 1000001):
        results.append((len(test(i)), i))
    results.sort(reverse=True)
    return results[0]
    
print find_longest()