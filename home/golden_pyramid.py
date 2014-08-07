from math import pow as pow
def count_gold(pyramid):
    
    # pos = 0
    # gold = pyramid[0][pos]
    # pyramid[0][pos] = 'x' # for testing with lists
    
    # initialize the val list
    vals = [ [0 for j in range(i+1)] for i in range(len(pyramid))]
    vals[0][0] = pyramid[0][0]
    # check_vals(vals)
    
    for row in range(len(pyramid)):
        for col in range(len(pyramid[row])):            
            print "row: %s | col: %s" %(row, col)
            if row!=0:
            
                
                
                if col >1 : # <<<<<<<<<< RIGHT HERE
                    
                    
                    
                    if pyramid[row-1][col] > pyramid[row-1][col-1]:
                        vals[row][col] = pyramid[row][col] + pyramid[row-1][col]
                    else:
                        vals[row][col] = pyramid[row][col] + pyramid[row-1][col-1]
    check_vals(vals)

    
    
    
    
    
    # ***************************************** #
    
    # for level in range(len(pyramid)):
        # if level+1 < len(pyramid):
            # if pos+1 < len(pyramid):
                # if pyramid[level+1][pos] > pyramid[level+1][pos+1]:
                    # gold+= pyramid[level+1][pos]
                    # pyramid[level+1][pos] = 'x' # for testing with lists
                    
                # else:
                    # gold+= pyramid[level+1][pos+1]
                    # pyramid[level+1][pos+1] = 'x' # for testing with lists
                    # pos+=1
        
        # # this prints each modified level
        # lvl_str = ''
        # for item in pyramid[level]:
            # lvl_str+= str(item)
        # print lvl_str
        # *******************************

    
    # ***************************************** #
    # print 'gold: %s' % gold
    # print "Routes: %s" % (int(pow(2,(len(pyramid)-1))))
    # return gold

# verify the val list is populated
def check_vals(vals):
    for level in vals:
        val_str = ''
        for val in level:
            val_str+= str(val)
        print val_str

if __name__ == '__main__':
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert count_gold([
        # [1,],
        # [2, 3],
        # [3, 3, 1],
        # [3, 1, 5, 4],
        # [3, 1, 3, 1, 3],
        # [2, 2, 2, 2, 2, 2],
        # [5, 6, 4, 5, 6, 4, 3]
    # ])
    assert count_gold([
        [1,],
        [2, 1],
        [1, 2, 1],
        [1, 2, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 2, 1, 1, 1, 1],
        [1, 2, 1, 1, 1, 1, 9]
    ])
    # assert count_gold((
        # (1,),
        # (2, 3),
        # (3, 3, 1),
        # (3, 1, 5, 4),
        # (3, 1, 3, 1, 3),
        # (2, 2, 2, 2, 2, 2),
        # (5, 6, 4, 5, 6, 4, 3)
    # )) == 23, "First example"
    # assert count_gold((
        # (1,),
        # (2, 1),
        # (1, 2, 1),
        # (1, 2, 1, 1),
        # (1, 2, 1, 1, 1),
        # (1, 2, 1, 1, 1, 1),
        # (1, 2, 1, 1, 1, 1, 9)
    # )) == 15, "Second example"
    # assert count_gold((
        # (9,),
        # (2, 2),
        # (3, 3, 3),
        # (4, 4, 4, 4)
    # )) == 18, "Third example"
