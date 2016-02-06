# -----------------
# User Instructions
#
# Write the max_wins function. You can make your life easier by writing
# it in terms of one or more of the functions that we've defined! Go
# to line 88 to enter your code.

from functools import update_wrapper
from collections import namedtuple
import random
import itertools

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

other = {1:0, 0:1}

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    if d == 1:
        return State(other[state.p], state.you, state.me+1, 0)
    else:
        return State(state.p, state.me, state.you, state.pending+d)

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    return State(other[state.p], state.you, state.me+state.pending, 0)

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

def Q_pig(state, action, Pwin):
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d)) for d in (2,3,4,5,6))) / 6.
    raise ValueError

def best_action(state, actions, Q, U):
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)

def pig_actions(state):
    "The legal actions from a state."
    return ['roll', 'hold'] if state.pending else ['roll']

goal = 40

@memo
def Pwin(state):
    """The utility of a state; here just the probability that an optimal player
    whose turn it is to move can win from the current state."""
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


def test():
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

strategies = [clueless, hold_at(goal/4), hold_at(1+goal/3), hold_at(goal/2),
    hold_at(goal), max_wins]

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
        else: 
			result = strategies[state.p](state)    
			if result == 'hold':        
				state = hold(state)
			elif result == 'roll':
				state = roll(state, next(dierolls))
			else:
				return strategies[other[state.p]]

other = {0:1, 1:0}
State = namedtuple('State', 'p me you pending')
goal = 50
possible_moves = ['roll', 'hold']

# first attemption to play tournament between strategies.
def play_tournament(strategies, n=500):
    A = itertools.permutations(strategies, 2)
    table = {}
    while n > 0:
        n = n - 1
        for x in A:
            #print (x[0].__name__,x[1].__name__)
            r = play_pig(x[0], x[1])
            try:
                table[r.__name__] = table[r.__name__] + 1
            except KeyError:
                table[r.__name__] = 1
    print table
    pass

if __name__=='__main__':
    #print test()
    play_tournament(strategies)
    play_tournament(strategies,50000)

