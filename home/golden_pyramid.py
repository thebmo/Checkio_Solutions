
def count_gold(pyramid):
    
    # initialize the val list
    vals = [ [0 for j in range(i+1)] for i in range(len(pyramid))]
    vals[0][0] = pyramid[0][0]
    
    
    # might be going about htis the wrong way (reverse order)
    for row in range(len(pyramid)):
        for col in range(len(pyramid[row])):            
            if row!=0:
                if col+1 > len(pyramid[row-1]): # <<<<<<<<<< RIGHT HERE                    
                    vals[row][col] += pyramid[row][col] + vals[row-1][col-1]
                else:
                    if pyramid[row-1][col] > pyramid[row-1][col-1]:
                        vals[row][col] += pyramid[row][col] + vals[row-1][col]
                    else:
                        vals[row][col] += pyramid[row][col] + vals[row-1][col-1]
    
    
    check_vals(vals)
    return max(vals[len(vals)-1])
    


# verify the val list is populated
def check_vals(vals):
    for level in vals:
        val_str = ''
        for val in level:
            val_str+= str(val) +' '
        print val_str


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