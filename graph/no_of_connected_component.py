def countComponents(n, edges):

    def dfs(node, adj_list, visited):
     
        if visited[node]:
            return

        visited[node] = True

        for elem in adj_list[node]:
            if not visited[elem]:
                dfs(elem, adj_list, visited)

    adj_list = [[] for _ in range(n)]
    for crs, pre in edges:
        adj_list[crs].append(pre)
        adj_list[pre].append(crs)

    visited = [False] * n

    connected = 0
    for node in range(n):
        if not visited[node]:
            connected += 1
            dfs(node=node, adj_list=adj_list, visited=visited)

    return connected


n = 5
edges =[[0,1],[1,2],[2,3],[3,4]]


n = 5
edges = [[0,1],[1,2],[3,4]]


n = 2
edges = [[1,0]]

result = countComponents(n, edges)
print(result)