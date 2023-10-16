def done_or_not(board):
    # rows
    for row in board:
        for i in range(1, 10):
            if i not in row:
                return 'Try again!'
    # columns
    for col in [[row[j] for row in board] for j in range(9)]:
        for i in range(1, 10):
            if i not in col:
                return 'Try again!'
    # squares
    rng = range(3)
    for square in [[board[3*i + x][3*j + y] for x in rng for y in rng] for i in rng for j in rng]:
        for i in range(1, 10):
            if i not in square:
                return 'Try again!'
    return 'Finished!'
