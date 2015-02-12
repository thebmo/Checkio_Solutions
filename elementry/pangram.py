def check_pangram(text):
    abc = []
    for t in text:
        if t.isalpha() and t.upper() not in set(abc):
            abc.append(t.upper())
    
    return True if len(abc) == 26 else False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
