def checkio(feed):
    bird_counter = 0
    fed = 0
    birds = []
    while (feed > 0):
        # bird configuration
        bird_counter+=1
        for i in range(bird_counter):
            birds.append(0)
        
        for bird in range(len(birds)):
            if feed > 0:
                feed-=1
                birds[bird]+=1
    
    # counts fed birds
    for bird in birds:
        if bird > 0:
            fed+=1

    return fed
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"