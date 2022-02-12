queue = []
visited = []
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

print(BFS(visited, graph, "A"))