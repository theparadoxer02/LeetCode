from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs():
            directions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]

            queue = deque([0, 0])

            while queue:
                x, y = queue.popleft()
                for left, right in directions:
                    new_x, new_y = x + left, y + right


s = Solution()
grid = []
result = s.shortestPathBinaryMatrix(grid=grid)
print(result)
