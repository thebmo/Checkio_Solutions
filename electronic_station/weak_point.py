def weak_point(matrix):
    min_row, min_col = 10000, 10000
    pos = [0,0]
    
    for x in range(len(matrix)):
        t_row  = sum(matrix[x])
        if t_row < min_row:
            min_row = t_row
            pos[0] = x
        t_col = 0
        for y in range(len(matrix)):
            t_col += matrix[y][x]
        if t_col < min_col:
            min_col = t_col
            pos[1] = x   
    return pos


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
