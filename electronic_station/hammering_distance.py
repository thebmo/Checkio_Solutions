def checkio(n, m):
    m = bin(m).replace('0b', '')
    n = bin(n).replace('0b', '')
    h = 0
    if len(m) > len(n):
        n = n.zfill(len(m))
    else:
        m = m.zfill(len(n))
    for i in range(len(m)):
        h+= abs(int(m[i]) - int(n[i]))

    return h

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
