from collections import deque

def rottingOranges(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    queue  = deque()
    fresh_oranges = 0

    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 2:
                queue.append((i, j))

            if grid[i][j] == 1:
                fresh_oranges += 1

    queue.append((-1, -1))
    minutes_elapsed = -1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        a, b = queue.popleft()
        if a == -1:
            minutes_elapsed += 1
            if queue:
                queue.append((-1, -1))
        else:
            for row, col in directions:
                adc_row = a + row
                adc_col = b + col
                if 0 <= adc_row < nrows and 0 <= adc_col < ncols and grid[adc_row][adc_col] == 1:
                    grid[adc_row][adc_col] = 2
                    fresh_oranges -= 1
                    queue.append((adc_row, adc_col))
    return minutes_elapsed if fresh_oranges == 0 else -1 



grid = [[2,1,1],[1,1,0],[0,1,1]]


result = rottingOranges(grid=grid)
print(result)
