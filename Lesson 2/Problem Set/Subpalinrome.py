# -*- coding: windows-1251 -*-
'''
Created on 28 окт. 2014 г.

@author: apushkar
'''

from recstring import RecString

# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    checkText = text.lower()
    minInd, maxInd, maxLen = 0, -1, -1
    for cc in range(1, len(checkText)):
        if cc < len(checkText) - 1:
            if checkText[cc-1] == checkText[cc+1]: #center of the odd palindrom is here
                for bc in range(0, cc):
                    if bc+cc+1 > len(checkText) - 1: break
                    if checkText[cc-bc-1] == checkText[cc+bc+1]:
                        if 2*bc+3 > maxLen:
                            minInd = cc-bc-1
                            maxInd = cc+bc+1
                            maxLen = maxInd - minInd + 1
                    else: break
        elif checkText[cc] == checkText[cc-1]: #center of the even palindrom is here
            for bc in range(0, cc):
                if bc+cc > len(checkText) - 1: break
                if checkText[cc-bc-1] == checkText[cc+bc]:
                    if 2*bc+2 > maxLen:
                        minInd = cc - bc - 1
                        maxInd = cc + bc
                        maxLen = maxInd - minInd + 1
                else: break
        else: break     
    return (minInd, maxInd+1)
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

if __name__ == '__main__':
#    print test()
    text = RecString('RacecarX')
    longest_subpalindrome_slice(text)
    print text.get_recording_link()