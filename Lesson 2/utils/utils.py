# -*- coding: windows-1251 -*-
'''
Created on 26 окт. 2014 г.
Utilities from different chapters
@author: Alexander
'''

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

''' tool for debugging '''
def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print '%s got %s with %5d iters over %7d items'%(fn.__name__, result, c.starts, c.items)
    
def c(sequence):
    """ Generate items in sequence; 
    keeping counts as we go. c.starts is the number of sequences started; 
    c.items is number of items generated
    """
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item    

if __name__ == '__main__':
    pass