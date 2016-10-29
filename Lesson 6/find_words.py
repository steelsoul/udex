def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

test_words()

# Alternative version

def find_words2(letters, pre='', results=None):
    if results is None: results=set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words2(letters.replace(L, '', 1), pre+L, results)
    return results
