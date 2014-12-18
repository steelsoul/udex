# -*- coding: windows-1251 -*-
'''
Created on 27 окт. 2014 г.

@author: apushkar
'''
from timeit import itertools
import string, re 

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                 for (i,d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

def compile_formula(formula, verbose = False):
    '''Compile formula into a function. Also return letters found, as a str, 
    in same orders as params of function. For example, 'YOU == ME**2' returns 
    (lambda Y, M, E, U, O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' '''
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (params, body)
    if verbose: print f
    return eval(f), letters 

def faster_solve(formula):
    """ Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula. """
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)): 
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError: 
            pass  
                

if __name__ == '__main__':
    print compile_word("YOU")
    print faster_solve("ODD + ODD == EVEN")
    pass