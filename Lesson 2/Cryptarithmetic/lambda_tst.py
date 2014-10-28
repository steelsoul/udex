# -*- coding: windows-1251 -*-
'''
Created on 27 окт. 2014 г.
@author: apushkar
'''

if __name__ == '__main__':
    ''' YOU == ME**2 '''
    f = lambda Y, M, E, U, O: (1*U + 10*O + 100*Y) == (1*E + 10*M)**2
    print f
    print f(1,2,3,4,5)
    print f(2,1,7,9,8)
    print 289 == 17**2    
    pass