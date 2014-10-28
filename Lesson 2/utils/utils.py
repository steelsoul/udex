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

if __name__ == '__main__':
    pass