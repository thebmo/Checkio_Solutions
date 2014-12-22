def translate(phrase):
    VOWELS = "aeiouy"
    phrase = phrase.lower()
    new_phrase = ''
    while len(phrase) > 0:
        new_phrase += phrase[0]
        if phrase[0] in VOWELS:
            phrase = phrase[3:]
        elif phrase[0] == ' ':
            phrase = phrase[1:]
        else:
            phrase = phrase[2:]
    return new_phrase

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
