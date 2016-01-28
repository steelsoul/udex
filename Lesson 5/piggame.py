# -*- coding: utf-8 -*-

# This code is based on "Design of Computer Programs" lesson 5.
# Please look at www.udacity.com

from collections import namedtuple
import random

def hold(state):
    return State(other[state.p], state.you, state.me+state.pending, 0)        

def roll(state, d):
    if d == 1:
        return State(other[state.p], state.you, state.me+1, 0)
    else:
        return State(state.p, state.me, state.you, state.pending+d)

possible_moves = ['roll', 'hold']        

# clueless strategy - just returns random move    
def clueless(state):
    return random.choice(possible_moves)

""" returns a strategy that holds if 
and only if pending >= x or player reaches goal """
def hold_at(x):
    def strategy(state):
        return 'hold' if (state.pending >= x or state.pending + state.me >= goal) else 'roll'
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy
    
def test():
    s = State(1,10,20,30)
    assert hold(s) == State(0,20,40,0)    
    assert roll(s,1) == State(0,20,11,0)
    assert roll(s,5) == State(1,10,20,35)
    assert hold_at(30)(State(1,29,15,20))=='roll'
    assert hold_at(30)(State(1,29,15,21))=='hold'
    assert hold_at(30).__name__=='hold_at(30)'
    assert hold_at(15)(State(0,2,30,10))=='roll'
    assert hold_at(15)(State(0,2,30,15))=='hold'

    
other = {0:1, 1:0}
State = namedtuple('State', 'p me you pending')
goal = 50    
    
if __name__=='__main__':
    test()
    print("test success")