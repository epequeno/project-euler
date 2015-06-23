# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:31:10 2011

@author: steven
"""

# from http://stackoverflow.com/a/18503368
def part(n, k):
    def memoize(f):
        cache = [[[None] * n for j in xrange(k)] for i in xrange(n)]
        def wrapper(n, k, pre):
            if cache[n-1][k-1][pre-1] is None:
                cache[n-1][k-1][pre-1] = f(n, k, pre)
            return cache[n-1][k-1][pre-1]
        return wrapper

    @memoize
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [(n,)]
            return []
        ret = []
        for i in xrange(min(pre, n), 0, -1):
            ret += [(i,) + sub for sub in _part(n-i, k-1, i)]
        return ret
    return _part(n, k, n)

def is_triple(x, y, z):
    return x**2 + y**2 == z**2

answer = [sorted(x) for x in list(part(1000, 3))]

for x in answer:
    if is_triple(x[0], x[1], x[2]):
        print x[0] * x[1] * x[2]
