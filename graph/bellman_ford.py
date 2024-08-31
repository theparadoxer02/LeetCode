from typing import List
from collections import defaultdict


def maxProbability(
    n: int,
    edges: List[List[int]],
    succProb: List[float],
    start_node: int,
    end_node: int,
) -> float:
    graph = []
    for i in range(len(edges)):
        u, v = edges[i]
        w = succProb[i]
        graph.append((u, v, w))
        graph.append((v, u, w))

    def bellman_ford(graph, start, n):
        distances = [float('inf')] * n
        distances[start] = 0

        for _ in range(n - 1):
            for u, v, w in graph:
                new_distance = distances[u] + w
                if new_distance < distances[v]:
                    distances[v] = new_distance

        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains a negative-weight cycle")
            return None
        
        return distances
    
    result = bellman_ford(
        graph,
        start=start_node,
        n=n
    )

    return result[end_node] if result[end_node] != 0 else 0.0


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

resutl = maxProbability(
    n=n, edges=flights, succProb=succProb, start_node=src, end_node=dst
)

print(resutl)