def safe_pawns(pawns):
    safe = 0
    board = [[0 for x in range(8)] for x in range(8)]
    
    for pawn in pawns:
        col = get_col(pawn[0])
        row = int(pawn[1])-1
        board[row][col]=1
    
    for i in range(len(board)):
        str_row = ''
        for j in range(len(board)):
            if board[i][j] > 0:
                if i!=0:
                    if j!=0 and board[i-1][j-1]:
                        board[i][j] = 'X'
                        safe+=1
                    elif j!=7 and board[i-1][j+1]:
                        board[i][j] = 'X'
                        safe+=1 
            str_row += str(board[i][j])
        print str_row
    print 'safe: %s \n' % safe
    return safe

    
def get_col(letter):
    col = {
            'a' : 0,
            'b' : 1,
            'c' : 2,
            'd' : 3,
            'e' : 4,
            'f' : 5,
            'g' : 6,
            'h' : 7
            }
    return col[letter]
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a1"}) == 0
    assert safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}) == 7
    assert safe_pawns({"a8","b7","c6","d5","e4","f3","g2","h1"}) == 7
    assert safe_pawns({"a1","a2","a3","a4","h1","h2","h3","h4"}) == 0
