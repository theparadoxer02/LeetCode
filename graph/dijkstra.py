import heapq


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
