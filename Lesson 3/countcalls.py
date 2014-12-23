# -*- coding: windows-1251 -*-
'''
Created on 23 дек. 2014 г.

@author: Alexander
'''

from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def countcalls(f):
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}

@decorator
def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)
    _f.cache = cache
    return _f

@countcalls
@memo
def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print "n\tfib(n)\tcalls"
    for i in range(31):
        a = fib(i)
        print '%d\t%d\t%d\t' % (i, a, callcounts[fib])
        callcounts[fib] = 0
    pass