# -*- coding: windows-1251 -*-
'''
Created on 28 окт. 2014 г.

@author: apushkar
'''

#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def adjacent(floor1, floor2):
    return abs(floor1 - floor2) == 1

# floor1 > floor2
def higher(floor1, floor2):
    return floor1 > floor2

def floor_puzzle():
    # Your code here
    floors = [bottom, _, middle, _, top] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))
    
    return  next(
            [Hopper, Kay, Liskov, Perlis, Ritchie] for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                if Hopper != top and Kay != bottom and Liskov != top and Liskov != bottom and higher(Perlis, Kay) 
                if not adjacent(Ritchie, Liskov) and not adjacent(Kay, Liskov)
            )

if __name__ == '__main__':
    print floor_puzzle()
    pass