import heapq


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:

    graph = {}
    for node in times:
        u, v, w = node[0], node[1], node[2]
        if u not in graph:
            graph[u] = {v: w}
        else:
            graph[u].update({v: w})

        if v not in graph:
            graph[v] = {}

    def dijkstra(graph, start):
        queue = []
        distances = {node: float("inf") for node in graph}

        distances[start] = 0
        heapq.heappush(queue, (0, start))

        while queue:
            curr_distance, curr_node = heapq.heappop(queue)

            if curr_distance > distances[curr_node]:
                continue
            
            for neighbor, weight in graph[curr_node].items():
                dist = weight + curr_distance

                if dist < distances[curr_node]:
                    distances[neighbor] = dist
                    heapq.heappush(queue, (dist, neighbor))

        return distances

    distances = dijkstra(graph, k)
    max_distance = max(distances.values())
    return max_distance if max_distance != float('inf') else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2



# times = [[1,2,1]]
# n = 2
# k = 1

# times = [[1,2,1]]
# n = 2
# k = 2


times = [[1,2,1],[2,1,3]]
n = 2
k = 2
result = networkDelayTime(times, n, k)
print(result)
