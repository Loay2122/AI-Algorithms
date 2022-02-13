import queue as Q

def BEST(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + " not found in graph!")
        return
    if end not in graph:
        raise TypeError(str(end) + " not found in graph!")
        return
    
    queue = Q.PriorityQueue()
    queue.put((int(graph[start]['heuristic']), [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1])-1]

        if end in node[1]:
            print("Path found: " + str(node[1]))
            break

        for neighbor in graph[current]['neighbors']:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((graph[neighbor]['heuristic'], temp))

def readGraph():
    lines = int(input("Please enter the Space State... \n"))
    graph={}

    for line in range(lines):
        line = input()
        tokens = line.split()
        node = tokens[0]
        graph[node]={}
        graph[node]['heuristic']=tokens[1]
        graph[node]['neighbors']=tokens[2:]
    return graph

def main():
    graph = readGraph()
    Start= input("Please enter the start... \n")
    End = input("Please enter the end destination... \n")
    BEST(graph, Start, End)

if __name__ == "__main__":
    main()

#Sample Input
# 6
# S 10 B A
# A 2 C D 
# B 3 D G 
# C 1
# D 4 C G 
# G 0 