from collections import deque

def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    
    if not board:
        return
    
    nrows = len(board)
    ncols = len(board[0])

    region_indexes = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(nrows):
        for j in range(ncols):
            if (i == 0 or j == 0 or i == nrows-1 or j == ncols-1) and board[i][j] == "O":
                region_indexes.append((i, j))

    def bfs(queue):
        while queue:
            a, b = queue.popleft()
            board[a][b] = True

            for x, y in directions:
                nx, ny = a + x, b + y
                
                if 0 < nx < nrows - 1 and 0 < ny < ncols -1 and board[nx][ny] == 'O' :
                    board[nx][ny] = True
                    queue.append((nx, ny))
        
    bfs(region_indexes)
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
