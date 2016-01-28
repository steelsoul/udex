# -*- coding: utf-8 -*-

# This code is based on "Design of Computer Programs" lesson 5.
# Please look at www.udacity.com

other = {0:1, 1:0}

#state: (p, me, you, pending)
def hold(state):
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)        

def roll(state, d):
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0)
    else:
        return (p, me, you, pending+d)
    
def test():
    s = (1,10,20,30)
    assert hold(s) == (0,20,40,0)    
    assert roll(s,1) == (0,20,11,0)
    assert roll(s,5) == (1,10,20,35)
    
if __name__=='__main__':
    test()
    print("test success")