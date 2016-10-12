
WORDS = set(file('words4k.txt').read().upper().split())

def find_words(hand):
    ''' Find all words that can be made from the letters in hand '''
    results = set()
    for a in hand:
        if a in WORDS: results.add(a)
        for b in removed(hand, a):
            w = a+b
            if w in WORDS: results.add(w)
            for c in removed(hand, w):
                w = a+b+c
                if w in WORDS: results.add(w)
                for d in removed(hand, w):
                    w = a+b+c+d
                    if w in WORDS: results.add(w)
                    for e in removed(hand, w):
                        w = a+b+c+d+e
                        if w in WORDS: results.add(w)
                        for f in removed(hand, w):
                            w = a+b+c+d+e+f
                            if w in WORDS: results.add(w)
                            for g in removed(hand, w):
                                w = a+b+c+d+e+f+g
                                if w in WORDS: results.add(w)
    return results

def removed(letters, remove):
    ''' Return a str of letters, but with each letter in remove removed once '''
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters
                                
                    
def prefixes(word):
    ''' A list of the initial sequences of a word, not including the word itself '''
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename) # opens file
    text = file.read()    # gets file into string
    # your code here
    wordset = set()
    prefixset = set()
    for word in set(text.upper().split()):
        wordset.add(word)
        [prefixset.add(w) for w in prefixes(word)]
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

def test():
    assert len(WORDS)    == 3892
    assert len(PREFIXES) == 6475
    assert 'UMIAQS' in WORDS
    assert 'MOVING' in WORDS
    assert 'UNDERSTANDIN' in PREFIXES
    assert 'ZOMB' in PREFIXES
    return 'tests pass'

assert prefixes('WORD') == ['', 'W', 'WO', 'WOR']
print test()
