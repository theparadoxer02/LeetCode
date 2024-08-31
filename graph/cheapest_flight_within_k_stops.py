from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    def bellman_ford(graph, start, k):
        distances = [float('inf')] * n
        distances[src] = 0
        for _ in range(k+1):
            new_distances = distances.copy()
            for u, v, w in graph:
                if distances[u] != float('inf') and (distances[u] + w) < new_distances[v]:
                    new_distances[v] = distances[u] + w
            distances = new_distances.copy()

        return distances

    graph = flights
    result = bellman_ford(graph, start=src, k=k)

    return result[dst] if result[dst] != float('inf') else -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

result = findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k)

print(result)
