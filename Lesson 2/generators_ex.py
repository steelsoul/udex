'''
Created on 24 oct. 2014
@author: apushkar
'''
# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    yield(0)
    for i in ints(1):
        yield(i)
        yield(-i)
        
if __name__ == "__main__":
    for i in all_ints(): print '%d '%i 
    pass
