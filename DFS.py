def Iteration_DFS(graph, start):
    stack = [start]
    visited = []
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return visited

def Recursive_DFS(graph, start, visited=[]):
    visited.append(start)
    for next in set(graph[start]) - set(visited):
        Recursive_DFS(graph, next, visited)
    return(visited)

graph = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": [],
    "H": [],
    "I": [],
    "J": []
}

print(Iteration_DFS(graph, start="A"))
print(Recursive_DFS(graph, start="A", visited=[]))