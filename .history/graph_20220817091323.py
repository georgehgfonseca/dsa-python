class Graph:
    def __init__(self, countNodes, countEdges=0):
        self.countNodes = countNodes
        self.countEdges = countEdges
        self.adjMatrix = [[0 for _ in range(countNodes)] for _ in range(countNodes)]

    def addEdge(self, source, sink):
        self.adjMatrix[source][sink] = 1
        self.countEdges += 1
