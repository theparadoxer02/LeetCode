class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) 

    def display(self):
        for node in self.graph:
            print(f'{node} -> {" ".join(str(neighbor) for neighbor in self.graph[node])}')


# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('A', 'C')
g.add_edge('C', 'D')
g.display()


def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(visited)

        for item in graph[node]:
            dfs(graph, item, visited)

dfs(g.graph, 'A', set())
