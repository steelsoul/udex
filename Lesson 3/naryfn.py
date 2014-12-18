# -*- coding: windows-1251 -*-
'''
Created on 16 дек. 2014 г.

@author: Alexander
'''
# import Compilers.one_of_and_alt
# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 


"""Given  binary function takes 2 inputs as input and returns an n_ary function 
such that f(x,y,z) = f(x, f(y, z)), etc . Also allow f(x) = x."""
def n_ary(f):
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

def seq(x,y): return seq('seq', x, y)

seq = n_ary(seq)
# 
# seq(lit('a'))
# seq(lit('b'), lit('c'))


def n_ary_mine(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        if not args: return x
        elif len(args) == 1: return f(x, args[0])
        result = f(args[len(args)-2], args[len(args)-1])
        for i in range(len(args)-1):
            b1 = x if len(args)-2-i == 0 else args[len(args)-3-i]
            result = f(b1, result)
        return result
    return n_ary_f

if __name__ == '__main__':
    pass