def maxAreaIsland(grid):

    if not grid:
        return 
    
    nrows = len(grid)
    ncols = len(grid[0])

    def dfs(i, j):
        if i < 0 or j < 0 or i >= nrows or j >= ncols or grid[i][j] == 0:
            return 0

        area = 1
        grid[i][j] = 0
        area += dfs(i - 1, j)
        area += dfs(i + 1, j)
        area += dfs(i, j - 1)
        area +=  dfs(i, j + 1)

        return area


    final_area = 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 1:
                current_area = dfs(i, j)
                final_area += current_area

    return final_area


grid = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

# grid =[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]

total_islands = maxAreaIsland(grid=grid)
print(total_islands)