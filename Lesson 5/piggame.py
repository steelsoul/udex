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

def always_roll(state):
    return 'roll'

def always_hold(state):
    return 'hold'

def dierolls():
	"Generate die rolls"
	while True:
		yield random.randint(1,6)

def play_pig(A, B, dierolls=dierolls()):
    """Play a game between 2 players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player. """
    state = State(0, 0, 0, 0)
    strategies = [A, B]
    while True:
		if state.me >= goal:
			return strategies[state.p]
		elif state.you >= goal:
			return strategies[other[state.p]]
		elif strategies[state.p](state) == 'hold':
			state = hold(state)
		else:
			state = roll(state, next(dierolls))   

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
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
	A, B = hold_at(50), clueless
	rolls = iter([6,6,6,6,6,6,6,6,2])
    assert play_pig(A, B, rolls)==A
    return 'tests pass'

other = {0:1, 1:0}
State = namedtuple('State', 'p me you pending')
goal = 50

if __name__=='__main__':
    print(test())
