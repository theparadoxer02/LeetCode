def findOrder(numCourses, prerequisites):
    ordering = []

    def dfs(node, adj_list, visited, pathVisited):
     
        if pathVisited[node]:
            return True

        if visited[node]:
            return False

        visited[node] = True
        pathVisited[node] = True

        for elem in adj_list[node]:
            if dfs(elem, adj_list, visited, pathVisited):
                return True

        pathVisited[node] = False
        ordering.append(node) 

        return False


    adj_list = [[] for _ in range(numCourses)]
    for crs, pre in prerequisites:
        adj_list[crs].append(pre) 

    visited = [False] * numCourses
    pathVisited = [False] * numCourses


    for node in range(numCourses):
        if dfs(node=node, adj_list=adj_list, visited=visited, pathVisited=pathVisited):
            return []

    return ordering



numCourses = 2
prerequisites = [[1,0]]

numCourses = 2
prerequisites = [[0,1]]

# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
result = findOrder(numCourses, prerequisites)
print(result)