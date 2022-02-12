#DFS
graph = {
    "1": ["2","3"],
    "2": ["1","4"],
    "3": ["1","5"],
    "4": ["2","5"],
    "5": ["3","4"]
}
queue = []
Visited=[]
def Recursive_DFS(graph, start, visited=[]):
    visited.append(start)
    for next in set(graph[start]) - set(visited):
        Recursive_DFS(graph, next, visited)
    return(visited)

#BFS
def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return(queue)
print(Recursive_DFS(graph, "1"))
print(BFS(Visited, graph, "1"))