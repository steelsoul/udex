'''
Created on 24 oct. 2014.

@author: apushkar
'''

import itertools
from utils.utils import timedcall

def imright(first, other):
    return other - first == 1

def nextto(first, other):
    return abs(other-first) == 1

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

## initialize c.starts and c.items
c.starts, c.items = 0, 0

def zebra_puzzle():
    houses = [first, _, middle, _, _] = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses)) #1
    return next((WATER, ZEBRA)
        for (red, green, ivory, yellow, blue) in c(orderings)
        if imright(green, ivory) #6
        for (Englishman, Spaniard, Ukrainian, Japanese, Norvegian) in c(orderings)
        if Englishman is red #2
        if Norvegian is first #10
        if nextto(Norvegian, blue) #15
        for (coffee, tea, milk, oj, WATER) in c(orderings)
        if coffee is green #4
        if Ukrainian is tea #5
        if milk is middle #9
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
        if Kools is yellow #8
        if LuckyStrike is oj #13
        if Japanese is Parliaments #14
        for (dog, snails, fox, horse, ZEBRA) in c(orderings)
        if Spaniard is dog #3
        if OldGold is snails #7
        if nextto(Chesterfields, fox) #11
        if nextto(Kools, horse) #12
        )
    
def zebra_puzzle_his():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )      

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    result = ()
    times = []
    if isinstance(n, int):
        if (result == ()): 
            temp, result = timedcall(fn, *args)
            times.append(temp)
        else: 
            times = [timedcall(fn, *args) for _ in range(n)]
    else:
        while sum(times) < n:
            if (result == ()): 
                temp, result = timedcall(fn, *args)
                times.append(temp)
            else: 
                times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times), result[0], result[1]

if __name__ == '__main__':
    answer1 = timedcalls(1, zebra_puzzle_his)
    print 'The Zebra Puzzle answer is (%d %d)' % (answer1[3],answer1[4])
    print 'Timing result:\n\tmin %03f average %03f and max %03f for 5 sec duration; result is (%d %d)' % (timedcalls(5.0, zebra_puzzle))
    instrument_fn(zebra_puzzle)
    