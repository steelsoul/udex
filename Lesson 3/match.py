# -*- coding: windows-1251 -*-
'''
Created on 08 нояб. 2014 г.

@author: Alexander
'''

def match(pattern, text):
    remainders = pattern(text)
    if remainders: 
        shortest = min(remainders, key=len)
        return text[:len(text) - len(shortest)]
    
def lit(s): return lambda t: set([t[len(s):]]) if t.startswith(s) else null
def seq(x,y): return lambda t: set().union(*map(y, x(t)))
def alt(x,y): return lambda t: x(t) | y(t)
def oneof(chars): return lambda t: set([t[1:]]) if (t and t[0] in chars) else null
dot = lambda t: set([t[1:]]) if t else null
eol = lambda t: set[''] if t == '' else null

null = frozenset([])

def star(x): return lambda t: (set([t]) | 
                               set(t2 for t1 in x(t) if t1 != t
                                   for t2 in star(x)(t1)))

def test():
    assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(lit('hello'), 'hello how are you?') == 'hello'
    assert match(lit('x'), 'hello how are you?') == None
    assert match(oneof('xyz'), 'x**2 + y**2 = r**2') == 'x'
    assert match(oneof('xyz'), '   x is here!') == None
    return 'tests pass'

if __name__ == '__main__':
    print test()
    pass