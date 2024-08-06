def dfsCheck(node, adj_node, visited, pathVisited):

    if pathVisited[node]:
        return True

    if visited[node]:
        return False

    
    visited[node] = True
    pathVisited[node] = True

    
    for i in adj_node[node]:
        if dfsCheck(node=i, adj_node=adj_node, visited=visited, pathVisited=pathVisited):
            return True


    pathVisited[node] = False
    return False
    

def canFinish(numCourses, prerequisites):

    adj_node = [[] for _ in range(numCourses)]
    for prerequisite in prerequisites:
        adj_node[prerequisite[1]].append(prerequisite[0])

    visited = [ False] * numCourses
    pathVisited= [False] * numCourses

    for node in range(numCourses):
        if dfsCheck(node=node, adj_node=adj_node, visited=visited, pathVisited=pathVisited):
            return False
    
    return True

numCourses = 2
prerequisites = [[1,0], [0, 1]]

print(canFinish(numCourses, prerequisites))