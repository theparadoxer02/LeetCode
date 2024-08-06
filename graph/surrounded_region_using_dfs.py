from collections import deque

def solve(board):
    
    if not board:
        return
    
    nrows = len(board)
    ncols = len(board[0])

    region_indexes = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def dfs(i, j):
        if i < 0 or j < 0 or i >= nrows or j >= ncols or board[i][j] == "X" or board[i][j] == True:
            return
            
        board[i][j] = True
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)


    
    for i in range(nrows):
        for j in range(ncols):
            if (i == 0 or j == 0 or i == nrows-1 or j == ncols-1) and board[i][j] == "O":
                dfs(i, j)


    for i in range(nrows):
        for j in range(ncols):
            if board[i][j] is True:
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'
    return board

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

new_board = solve(board=board)

print(new_board)
