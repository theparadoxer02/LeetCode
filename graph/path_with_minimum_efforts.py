from typing import List


def minimumEffortPath(heights: List[List[int]]) -> int:
    def bellman_ford(graph, start, k):
        distances = [float('inf')] * len(graph)
        distances[start] = 0

        for _ in range(len(heights)):
            for u, v, w in graph:
                new_distance = distances[u] + w
                if new_distance < distances[v]:
                    distances[v] = new_distance
                
        return distances
            
    M = len(heights)
    N = len(heights[0])
    # weight_graph = [[float('inf')] * N for _ in range(M)]
    weight_graph = []

    for i in range(M):
        for j in range(N):
            if j + 1 < N:
                weight_graph.append([heights[i][j], heights[i][j+1], heights[i][j+1] - heights[i][j]])

            if i + 1 < M:
                weight_graph.append([heights[i][j], heights[i+1][j], heights[i+1][j] - heights[i][j]])
    
    n = len(heights)
    result = bellman_ford(weight_graph, start=1, k=n)
    return min(result)


heights = [[1,2,2],[3,8,2],[5,3,5]]
# heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5], [5, 3, 5]]

result = minimumEffortPath(heights=heights)

print(result)
