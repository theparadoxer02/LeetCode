from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]
        visited = set()
        m, n = len(image), len(image[0])

        def dfs(i, j):

            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != curr_color or (i, j) in visited:
                return

            image[i][j] = color
            visited.add((i, j))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for x, y in directions:
                new_x, ney_y = x + i, y + j
                dfs(new_x, ney_y)

        dfs(sr, sc)
        return image


s = Solution()
image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
result = s.floodFill(image=image, sr=sr, sc=sc, color=0)
print(result)
