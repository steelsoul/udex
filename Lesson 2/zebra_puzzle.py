'''
Created on 23 oct. 2014.

@author: Alexander
'''

import itertools
import time
from utils.utils import timedcall

# Returns true if item is to the right of the item2
def imright(item1, item2):
    return item2 - item1 == 1

def nextto(item1, item2):
    return abs(item1 - item2) == 1


def zebra_puzzle():
    houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    
    a = 0
    curr = 0.0
    
    for (red, green, ivory, yellow, blue) in orderings:
        print "Current progress is:", curr/5.0, "iteration:", a
        for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings:
            for (dog, snails, fox, horse, ZEBRA) in orderings:
                for (coffee, tea, milk, oj, WATER) in orderings:
                    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                        a = a + 1
                        if (Englishman is red): 
                            if (Spaniard is dog):
                                if (coffee is green):
                                    if (Ukrainian is tea): 
                                        if (imright(green, ivory)):
                                            if (OldGold is snails):
                                                if (Kools is yellow):
                                                    if (milk is middle):
                                                        if (Norwegian is first):
                                                            if nextto(Chesterfields, fox):
                                                                if nextto(Kools, horse):
                                                                    if LuckyStrike is oj:
                                                                        if Japanese is Parliaments:
                                                                            if nextto(Norwegian, blue): 
                                                                                print "Water drinks:", WATER, "Zebra owns: ", ZEBRA
                                                                                return (WATER, ZEBRA)
        curr += 1.0 
                                                                            
def t():
    t0 = time.clock()
    zebra_puzzle()
    t1 = time.clock()
    return t1-t0

(timeres, result) = timedcall(zebra_puzzle)
print "The time to finish brute force was:", timeres