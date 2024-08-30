from collections import deque


def pacificAtlantic(heights):

    if not heights:
        return []

    nrows = len(heights)
    ncols = len(heights[0])

    can_flow_pacific = [[False] * ncols for _ in range(nrows)]
    can_flow_atlantic = [[False] * ncols for _ in range(nrows)]

    pacific_nodes = deque()
    atlantic_nodes = deque()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(nrows):
        for j in range(ncols):
            if i == 0 or j == 0:
                can_flow_pacific[i][j] = True
                pacific_nodes.append((i, j))

            if i == nrows - 1 or j == ncols - 1:
                can_flow_atlantic[i][j] = True
                atlantic_nodes.append((i, j))

    def bfs(queue, can_flow):
        while queue:
            a, b = queue.popleft()

            for x, y in directions:
                nx, ny = a + x, b + y

                if (
                    0 <= nx < nrows
                    and 0 <= ny < ncols
                    and not can_flow[nx][ny]
                    and heights[nx][ny] >= heights[a][b]
                ):
                    can_flow[nx][ny] = True
                    queue.append((nx, ny))

    bfs(pacific_nodes, can_flow_pacific)
    bfs(atlantic_nodes, can_flow_atlantic)

    result = [
        (i, j)
        for i in range(nrows)
        for j in range(ncols)
        if can_flow_pacific[i][j] and can_flow_atlantic[i][j]
    ]
    return result


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]

result = pacificAtlantic(heights=heights)
print(result)
