from typing import List
import time


def validPath(
    n: int, edges: List[List[int]], source: int, destination: int
) -> bool:

    if not edges:
        return True

    def dfs(graph, node, visited):
        if node not in visited:
            visited.add(node)
            print(visited)

            for item in graph[node]:
                dfs(graph, item, visited)

    graph = {}
    for edge in edges:
        u, v = edge[0], edge[1]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
        
    visited = set()
    dfs(graph, source, visited)

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
print("Process finished --- %s seconds ---" % (time.time() - start_time))

