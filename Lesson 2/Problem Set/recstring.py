# -*- coding: windows-1251 -*-
'''
@author: alebedev
'''

import json
 
class RecString(str):
    def __init__(self, text):
        self.steps = [text]
        self.index = 0
        
    def __eq__(self, other):
        if other is '':
            return not len(self)
        
        if len(self) != 1 or len(other) != 1 or not isinstance(other, RecString):
            self.error()
            
        equal = str.__eq__(self, other)
        self.steps.append(['c', self.index, other.index, 1 if equal else 0])
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, *args):
        if (len(args) > 1):
            self.error()
        else:
            return self.baby(str.__getitem__(self, *args), args[0])

    def __getslice__(self, *args):
        self.error()

    def lower(self):
        return self.baby(str.lower(self), self.index)

    def upper(self):
        return self.baby(str.upper(self), self.index)

    def baby(self, text, index):
        baby = RecString(text)
        baby.steps = self.steps
        baby.index = index
        return baby

    def error(self):
        raise Exception("""
        Please access only individual characters: e.g. text[a]
        Comparisons such as text == text[::-1] are O(n),
        do them explicitly one character at a time.
        """)

    def get_recording_link(self):
        return ('http://explored.tk/experiments/palindrome#[%s]' %
                json.dumps(self.steps, separators=(',',':')))
        