from collections import deque
from typing import Dict, Set, TypeVar, Generic, Deque


def bfs(graph: Dict, start: str, visited: set) -> None:
    queue = deque([start])

    while queue:
        print(f"{queue} visited: {visited}")
        leftest_element = queue.popleft()
        if leftest_element not in visited:
            visited.add(leftest_element)

            for element in graph[leftest_element]:
                queue.append(element)




graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A', set())