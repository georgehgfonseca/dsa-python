class Graph:
    def __init__(self, countNodes, countEdges=0):
        self.countNodes = countNodes
        self.countEdges = countEdges
        self.adjMatrix = [[0 for _ in range(countNodes)] for _ in range(countNodes)]
        self.adjList = [[] for _ in range(countNodes)]

    def addEdge(self, s, t):
        self.adjMatrix[s][t] = 1
        self.adjList[s].append(t)
        self.countEdges += 1

    def addUndirectedEdge(self, s, t):
        self.adjMatrix[s][t] = 1
        self.adjMatrix[t][s] = 1
        self.adjList[s].append(t)
        self.adjList[t].append(s)
        self.countEdges += 2

    def bfs(self, s):
        """Returns the visiting order of nodes from source s through bfs"""
        found = [0 for i in self.countNodes]  # i-th node has been found?
        Q = [s]  # Queue of nodes to explore
        R = [s]  # Visiting order
        found[s] = 1
        while Q:
            u = Q.pop(0)
            for v in self.adjList[u]:
                if found[v] == 0:
                    Q.append(v)
                    R.append(v)
                    found[v] = 1
        return R

    def dfs(self, s):
        """Returns the visiting order of nodes from source s through dfs"""
        found = [0 for i in range(self.size_v)]  # i-th node has been found?
        S = [s]  # Stack of nodes to explore
        R = [s]  # Visiting order
        found[s] = 1
        while S:
            u = S[-1]
            unstack = True
            for v in self.adj_list[u]:
                if found[v] == 0:
                    unstack = False
                    S.append(v)
                    R.append(v)
                    found[v] = 1
                    break
            if unstack:
                S.pop(-1)
        return R
