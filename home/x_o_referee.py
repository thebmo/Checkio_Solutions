def test(game_result):
    # cross strings
    crs1 = ''
    crs2 = ''
    
    # row column checking
    for x in range(0, len(game_result)):
        crs1 += game_result[x][x]
        crs2 += game_result[x][(len(game_result)-1)-x]
        if (game_result[x].count('X', 0, len(game_result)) == 3) or (game_result[x].count('O', 0, len(game_result)) == 3):
            return game_result[x][x]
        for y in range(0, len(game_result[x])):
            if x > 0:
                if (game_result[x][y] == game_result[x-1][y]) and (game_result[x][y] != '.'):
                    if x == len(game_result[x])-1 and game_result[x][y] == game_result[0][y]:
                        return game_result[x][y]
                else:
                    break
    # diaganol checks
    if (crs1.count('X', 0, len(crs1)) == 3) or (crs1.count('O', 0, len(crs1)) == 3):
        return crs1[0]
    
    elif (crs2.count('X', 0, len(crs2)) == 3) or (crs2.count('O', 0, len(crs2)) == 3):
        return crs2[0]

    else:
        return 'D'

def main():
    # game_result=[u"X.O",u"XX.",u"XOO"]
    # game_result=[u"X.O",u".O.",u"OO."]
    # game_result=[u"O.O",u"XX.",u"XXO"]
    game_result = ["OO.","XOX","XOX"]
    print test(game_result) + " wins"
        
if __name__ == "__main__":
    main()