# -*- coding: windows-1251 -*-
'''
Created on 26 окт. 2014 г.
@author: Alexander

usage: 
    python -m cProfile Cryptarithmetic\test_bf_solution.py  -- without cProfile import
    python -m Cryptarithmetic.test_bf_solution  -- with cProfile imported and added cProfile.run('test(2)') 
'''

import time
#import cProfile
from utils.utils import timedcall
from Cryptarithmetic.brute_force_solution import solve
from Cryptarithmetic.solution_opt import faster_solve

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP))==BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def test(fn, amount=1): 
    t0 = time.clock()
    for _ in range(0,amount):
        for example in examples: 
            print; print 11*' ',example
            print '%6.4f sec: %s' % timedcall(fn, example)
    print '%6.4f tot.' % (time.clock()-t0)
    return time.clock()-t0
    

if __name__ == '__main__':
    print 'Testing brute force solution: '
    t1 = test(solve, 2)
    print 'Testing optimized solution: '
    t2 = test(faster_solve, 2)
#    cProfile.run('test(2)')
    print 'Second solution is %3.0f times faster' % (t1/t2)