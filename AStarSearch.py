import queue as Q

def Astar(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + " not found in graph!")
        return
    if end not in graph:
        raise TypeError(str(end) + " not found in graph!")
        return
    
    queue = Q.PriorityQueue()
    queue.put((int(graph[start]['heuristic']), [start]))
    visited = []

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1])-1]

        if end in node[1]:
            print("Path found: " + str(node[1]))
            break

        for neighbor in graph[current]['neighbors']:
            temp = node[1][:]
            temp.append(neighbor[0])
            cost = int(graph[neighbor[0]]['heuristic'])+node[0]-int(graph[current]['heuristic'])+neighbor[1]
            queue.put((cost, temp))

def readGraph():
    lines = int(input("Please enter the Space State... \n"))
    graph={}

    for line in range(lines):
        line = input()
        tokens = line.split()
        node = tokens[0]
        graph[node]={}
        graph[node]['heuristic']=tokens[1]
        graph[node]['neighbors']=[]
        for i in range(2,len(tokens)-1, 2):
            graph[node]['neighbors'].append((tokens[i],int(tokens[i+1])))
    return graph

def main():
    graph = readGraph()
    Start= input("Please enter the start... \n")
    End = input("Please enter the end destination... \n")
    Astar(graph, Start, End)

if __name__ == "__main__":
    main()

#Sample Input:
# 5
# S 7 B 2 A 1
# A 6 B 2 C 5 G 0
# B 2 C 1
# C 1 G 3
# G 0