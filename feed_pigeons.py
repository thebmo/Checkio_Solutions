def checkio(number):
    bird_counter = 0
    fed = 0
    birds = 0
    while(number > 0):
        bird_diff = bird_counter*2
        bird_counter +=1
        birds += bird_counter
        if (birds + bird_diff) <= number:
            fed += bird_counter
        else:
            break
    print fed
    print '\n\n'
    return fed
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"