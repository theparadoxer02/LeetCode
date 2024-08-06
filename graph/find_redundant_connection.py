def findRedundantConnection(edges):

    def dfsCheck(node, adj_list, visited, parent):
        visited[node] = True
        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                t = dfsCheck(node=neighbour, adj_list=adj_list, visited=visited, parent=node)
                if t:
                    return t
            elif neighbour != parent:
                return [parent, node]
        return False

    n = len(edges)

    adj_list = [[] for _ in range(n + 1)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

        visited = [False] * (n + 1)
        if dfsCheck(edge[0], adj_list, visited, -1):
            return edge

    return []

edges = [[1, 2], [1, 3], [2, 3]]
print(findRedundantConnection(edges))  # Expected output: [2, 3]
