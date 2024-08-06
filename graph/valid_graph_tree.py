def validTree(n, edges):

    def dfsCheck(node, adj_list, visited, parent):

        visited[node] = True

        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                if dfsCheck(node=neighbour, adj_list=adj_list, visited=visited, parent=node):
                    return True
            
            elif neighbour != parent:
                return True

        return False
    

    # check if number of edges is not equal to n - 1 
    if len(edges) != n - 1:
        return False
    
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[1]].append(edge[0])
        adj_list[edge[0]].append(edge[1])

    visited = [ False] * n

    # start from the first node, return if cycle exists else it will automatically traverse all the nodes
    if dfsCheck(0, adj_list, visited, -1):
        return False

    for v in visited:
        if not v:
            return False

    return True


n = 5
edges = [[0, 1],[0, 2],[0, 3],[1, 4]]


# n = 5
# edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]



n = 5
edges = [[0,1],[0,4],[1,4],[2,3]]

result = validTree(n=n, edges=edges)


print(result)