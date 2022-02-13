import queue as Q

class Heuristic:
    def __init__(self, val):
        self.val = val
        self.graph={}
        self.start = None
        self.end = None

    def readGraph_Astar(self):
        lines = int(input("Please enter the Space State... \n"))
        self.graph={}

        for line in range(lines):
            line = input()
            tokens = line.split()
            node = tokens[0]
            self.graph[node]={}
            self.graph[node]['heuristic']=tokens[1]
            self.graph[node]['neighbors']=[]
            for i in range(2,len(tokens)-1, 2):
                self.graph[node]['neighbors'].append((tokens[i],int(tokens[i+1])))
        return self.graph
    
    def readGraph_Best(self):
        lines = int(input("Please enter the Space State... \n"))
        self.graph={}

        for line in range(lines):
            line = input()
            tokens = line.split()
            node = tokens[0]
            self.graph[node]={}
            self.graph[node]['heuristic']=tokens[1]
            self.graph[node]['neighbors']=tokens[2:]
        return self.graph

    def Astar(self):
        if self.start not in self.graph:
            raise TypeError(str(self.start) + " not found in self.graph!")
            return
        if self.end not in self.graph:
            raise TypeError(str(self.end) + " not found in self.graph!")
            return
        
        queue = Q.PriorityQueue()
        queue.put((int(self.graph[self.start]['heuristic']), [self.start]))
        visited = []

        while not queue.empty():
            node = queue.get()
            current = node[1][len(node[1])-1]

            if self.end in node[1]:
                print("Path found: " + str(node[1]))
                break

            for neighbor in self.graph[current]['neighbors']:
                temp = node[1][:]
                temp.append(neighbor[0])
                cost = int(self.graph[neighbor[0]]['heuristic'])+node[0]-int(self.graph[current]['heuristic'])+neighbor[1]
                queue.put((cost, temp))


    def BEST(self):
        if self.start not in self.graph:
            raise TypeError(str(self.start) + " not found in self.graph!")
            return
        if self.end not in self.graph:
            raise TypeError(str(self.end) + " not found in self.graph!")
            return
        
        queue = Q.PriorityQueue()
        queue.put((int(self.graph[self.start]['heuristic']), [self.start]))

        while not queue.empty():
            node = queue.get()
            current = node[1][len(node[1])-1]

            if self.end in node[1]:
                print("Path found: " + str(node[1]))
                break

            for neighbor in self.graph[current]['neighbors']:
                temp = node[1][:]
                temp.append(neighbor)
                queue.put((self.graph[neighbor]['heuristic'], temp))

def main():
    n = 1
    while n == 1 or n == 2:
        n = int(input("Please enter 1 for A* search or 2 for Best first search or any number to exit... \n"))
        if n==1:
            stateSpace = Heuristic(1)
            stateSpace.readGraph_Astar()
            stateSpace.start = input("Please enter the start... \n")
            stateSpace.end = input("Please enter the end destination... \n")
            stateSpace.Astar()
        elif n == 2:
            stateSpace = Heuristic(0)
            stateSpace.readGraph_Best()
            stateSpace.start = input("Please enter the start... \n")
            stateSpace.end = input("Please enter the end destination... \n")
            stateSpace.BEST()

main()

#Sample input for A*:
# 5
# S 7 B 2 A 1
# A 6 B 2 C 5 G 0
# B 2 C 1
# C 1 G 3
# G 0

#Sample input for Best First:
# 6
# S 10 B A
# A 2 C D 
# B 3 D G 
# C 1
# D 4 C G 
# G 0 