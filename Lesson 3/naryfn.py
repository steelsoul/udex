# -*- coding: windows-1251 -*-
'''
Created on 16 дек. 2014 г.

@author: Alexander
'''

from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

"""Given  binary function takes 2 inputs as input and returns an n_ary function 
such that f(x,y,z) = f(x, f(y, z)), etc . Also allow f(x) = x."""
@decorator
def n_ary(f):
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

@n_ary
def seq(x,y): return seq('seq', x, y)

if __name__ == '__main__':
    print help(seq)
    print 'test pass'
