# diag-top-left-to-bottom-right: matrix[x][x]
# diag-top-right-to-bottom-left: matrix[len(matrix[x])-x][x]


def checkio(matrix):
    c = 0
    r = 0
    d_t = 0
    d_b = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if y > 0:
                if matrix[x][y] == matrix[x][y-1]:
                    print "1: %s | 2: %s" %(matrix[x][y], matrix[x][y-1])
                    r+=1
                else: r=0
                
                if matrix[y][x] == matrix[y-1][x]:
                    c+=1
                else: c=0
                
                
                # if x < (len(matrix)-2) and matrix[len(matrix[x])-1-x][y] == matrix[len(matrix[x])-1-y][y+1]:
                            # d_b+=1
                # else: d_b = 0
                
                # if matrix[x][x] == matrix[x-1][x-1]:
                    # print 'x: %s | y: %s' % (matrix[x][x],matrix[x-1][x-1])
                    # d_t+=1
                # else: d_t = 0
            
        
                if c>2 or r>2 or d_t>2 or d_b>2:
                    print 'c: %s | r: %s | t: %s | b: %s - True' % (c,r,d_t,d_b)
                    return True

        
    print 'c: %s | r: %s | t: %s | b: %s - False' % (c,r,d_t,d_b)    
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [2, 3, 4, 5],
        [2, 3, 4, 5],
        [1, 1, 1, 1],
        [2, 3, 4, 5]
    ]) == True, "Horizontal"
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    
    assert checkio([
        [2,7,6,2,1,5,2,8,4,4],
        [8,7,5,8,9,2,8,9,5,5],
        [5,7,7,7,4,1,1,2,6,8],
        [4,6,6,3,2,7,6,6,5,1],
        [2,6,6,9,8,5,5,6,7,7],
        [9,4,1,9,1,3,7,2,3,1],
        [5,1,4,3,6,5,9,3,4,1],
        [6,5,5,1,7,7,8,2,1,1],
        [9,5,7,8,2,9,2,6,9,3],
        [8,2,5,7,3,7,3,8,6,2]
    ]) == False, "last"
