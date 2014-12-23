'''
Created on  12/24/2014.
@author: Alexander
'''
# ---------------
# User Instructions
#
# Modify the function, trace, so that when it is used
# as a decorator it gives a trace as shown in the previous
# video. You can test your function by applying the decorator
# to the provided fibonnaci function.
#
# Note: Running this in the browser's IDE will not display
# the indentations.

from functools import update_wrapper


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result = f(args[0])
            if result == 1:
                print '%s<-- %s == %s' % ((trace.level-1)*indent, signature, result)
            trace.level -= 1
        finally:
            if result == 0: 
                print '%s<-- %s == %s' % ((trace.level)*indent,signature,args[0])
            # your code here
        return 0# your code here
    trace.level = 0
    return _f

@trace
def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)

if __name__ == '__main__':
    fib(6)
    pass