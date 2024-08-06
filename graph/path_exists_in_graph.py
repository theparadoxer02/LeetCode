graph = {}

def generate_graph(edge):
    u, v = edge[0], edge[1]
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u) 



def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(visited)

        for item in graph[node]:
            dfs(graph, item, visited)


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2


n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

for edge in edges:
    generate_graph(edge)

visited = set()
dfs(graph, source, visited)


print(destination in visited)





class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if not edges:
            return True

        graph = {}

        def generate_graph(edge):
            u, v = edge[0], edge[1]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u) 

        def dfs(graph, node, visited):
            if node not in visited:
                visited.add(node)
                print(visited)

                for item in graph[node]:
                    dfs(graph, item, visited)

        for edge in edges:
            generate_graph(edge)

        visited = set()
        dfs(graph, source, visited)

        return destination in visited