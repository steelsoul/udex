# -*- coding: utf-8 -*-

# This code is based on "Design of Computer Programs" lesson 5.
# Please look at www.udacity.com

from collections import namedtuple
from functools import update_wrapper
import random

def decorator(d):
    "Make function d a decoratorL d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that catches the return value for each call to f(args).
    Then when called again with the same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some elements of args cannot be a dict key
            return f(args)
    return _f



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

def Q_pig(state, action, Pwin):
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d)) for d in (2,3,4,5,6))) / 6.
    raise ValueError

def pig_actions(state):
    "The legal actions from a state"
    return ['roll', 'hold'] if state.pending else ['roll']

@memo
def Pwin(state):
    """The utility of a state; here just the probability that an optimal player
    whoose turn is to move can win from the current state."""
    # Assumes opponent also plays with optimal strategy.
    if state.me + state.pending >= goal:
        return 1
    elif state.you >= goal:
        return 0
    else:
        return max(Q_pig(state, action, Pwin)
                   for action in pig_actions(state))

def max_wins(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state, pig_actions, Q_pig, Pwin)

@memo
def win_diff(state):
    "The utility of a state: here the winning differential (pos or neg)."
    (p, me, you, pending) = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    else:
        return max(Q_pig(state, action, win_diff)
                   for action in pig_actions(state))

def max_diffs(state):
    """A strategy that maximizes the expected difference between my final score
    and my opponent's."""
    return best_action(state, pig_actions, Q_pig, win_diff)

def best_action(state, actions, Q, U):
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key = EU)

def test_max_wins():
    assert max_wins(State(1, 5, 34, 4)) == 'roll'
    assert max_wins(State(1, 18, 27, 8)) == 'roll'
    assert(max_wins(State(0, 23, 8, 8)))   == "roll"
    assert(max_wins(State(0, 31, 22, 9)))  == "hold"
    assert(max_wins(State(1, 11, 13, 21))) == "roll"
    assert(max_wins(State(1, 33, 16, 6)))  == "roll"
    assert(max_wins(State(1, 12, 17, 27))) == "roll"
    assert(max_wins(State(1, 9, 32, 5)))   == "roll"
    assert(max_wins(State(0, 28, 27, 5)))  == "roll"
    assert(max_wins(State(1, 7, 26, 34)))  == "hold"
    assert(max_wins(State(1, 20, 29, 17))) == "roll"
    assert(max_wins(State(0, 34, 23, 7)))  == "hold"
    assert(max_wins(State(0, 30, 23, 11))) == "hold"
    assert(max_wins(State(0, 22, 36, 6)))  == "roll"
    assert(max_wins(State(0, 21, 38, 12))) == "roll"
    assert(max_wins(State(0, 1, 13, 21)))  == "roll"
    assert(max_wins(State(0, 11, 25, 14))) == "roll"
    assert(max_wins(State(0, 22, 4, 7)))   == "roll"
    assert(max_wins(State(1, 28, 3, 2)))   == "roll"
    assert(max_wins(State(0, 11, 0, 24)))  == "roll"
    return 'tests pass'


from collections import defaultdict	

def story(): 
	states = [State(0, me, you, pending)
	for me in range(41) for you in range(41) for pending in range(41)
	if me + pending <= goal]
	
	r = defaultdict(lambda: [0,0])
	for s in states:
		w, d = max_wins(s), max_diffs(s)
		if w != d: 
			i = 0 if (w=='roll') else 1
			r[s.pending][i] += 1
	for (delta, (wrolls, drolls)) in sorted(r.items()):
		print ('%4d: %3d %3d' % (delta, wrolls, drolls))

if __name__=='__main__':
    print(test())
    goal = 40
    print(test_max_wins())
    story()
