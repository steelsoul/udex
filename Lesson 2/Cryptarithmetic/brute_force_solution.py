# -*- coding: windows-1251 -*-
'''
Created on 25 ���. 2014 �.
@author: Alexander
'''

from __future__ import division
import string, re, itertools

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits"
    letters = "".join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def valid(f): 
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f): return f
        
def solve_all(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f): yield f
            
if __name__ == '__main__':
    print 'solve once: '
    print solve('ODD + ODD == EVEN')
    print 'solve all: '
    for a in solve_all('ODD + ODD == EVEN'): print a    
    pass