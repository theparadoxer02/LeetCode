from typing import List
import time


def validPath(
    n: int, edges: List[List[int]], source: int, destination: int
) -> bool:

    if source == destination:
        return True

    visited = set()

    def dfs(graph, node):
        if node not in visited:
            visited.add(node)

            for item in graph[node]:
                dfs(graph, item)

    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    dfs(graph, source)
    return destination in visited


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2


n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5


start_time = time.time()
result = validPath(n=n, edges=edges, source=source, destination=destination)
print(result)
# print("Process finished --- %s seconds ---" % (time.time() - start_time))

