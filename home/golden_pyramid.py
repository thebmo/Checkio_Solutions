# counts the gold
def count_gold(pyramid):
    p = pyramid
    t = []
    off_sets = [0, 1]
    
    #creates an empty copy of the pyramid
    for i in range(0, len(p)):
        zeros = []
        for j in range(0, i+1):
            zeros.append(0)
        t.append(zeros)

    for x, row in enumerate(p):
        for y, col, in enumerate(row):
            if x == 0 and y == 0:
                t[x][y] = p[x][y]
            
            for o in off_sets:

                try:
                    if t[x][y] + p[x+1][y+o] > t[x+1][y+o]:
                        t[x+1][y+o] = t[x][y] + p[x+1][y+o]
                
                except:
                    pass

    print '\nMAX GOLD:', max(t[len(t)-1]), '\n'
    return max(t[len(t)-1])


# creates a pyramid with specified levels and max gold per
# room if specifed, this is for testing time
def create_pyramid(levels, MAX=1000):
    from random import randrange as rand
    pyramid = []
    for L in range(0, levels):
        level = []
        for i in range(0, L+1):
            level.append(rand(1,MAX))
        pyramid.append(tuple(level))
    
    return tuple(pyramid)
        

if __name__ == '__main__':
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
    assert count_gold((
        (6,),
        (6,9),
        (7,1,4),
        (6,9,9,7),
        (1,6,7,9,7),
        (5,7,2,6,0,9),
        (1,2,2,6,0,1,6),
        (8,5,0,3,1,4,3,1),
        (9,6,4,1,1,9,3,7,9),
        (5,8,4,3,5,4,5,1,8,3))) == 66, "fourth example"
    count_gold(create_pyramid(10)