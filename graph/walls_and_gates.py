from collections import deque


class Solution:
    IMF = 2147483647
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return
        
        nrows = len(rooms)
        ncols = len(rooms[0])

        queue = deque()
    
        for i in range(nrows):
            for j in range(ncols):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            a, b = queue.popleft()

            for x, y in directions:
                new_row_index, new_col_index = a+x, b+y

                if 0 <= new_row_index < nrows and 0 <= new_col_index < ncols and rooms[new_row_index][new_col_index] == INF:
                    rooms[new_row_index][new_col_index] = rooms[a][b] + 1
                    queue.append((new_row_index, new_col_index))


rooms = [
    [float('inf'), -1, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), -1],
    [float('inf'), -1, float('inf'), -1],
    [0, -1, float('inf'), float('inf')]
]
sol = Solution()
