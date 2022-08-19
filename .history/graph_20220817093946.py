class Graph:
    def __init__(self, countNodes, countEdges=0):
        self.countNodes = countNodes
        self.countEdges = countEdges
        self.adjMatrix = [[0 for _ in range(countNodes)] for _ in range(countNodes)]
        self.adjList = [[] for _ in range(countNodes)]

    def addEdge(self, s, t):
        if s < self.countNodes and s >= 0 and t < self.countNodes and t >= 0:
            self.adjMatrix[s][t] = 1
            self.adjList[s].append(t)
            self.countEdges += 1

    def addUndirectedEdge(self, s, t):
        if s < self.countNodes and s >= 0 and t < self.countNodes and t >= 0:
            self.adjMatrix[s][t] = 1
            self.adjMatrix[t][s] = 1
            self.adjList[s].append(t)
            self.adjList[t].append(s)
            self.countEdges += 2

    def bfs(self, s):
        """Returns the visiting order of nodes from source s through bfs"""
        found = [0 for i in range(self.countNodes)]  # i-th node has been found?
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
        found = [0 for i in range(self.countNodes)]  # i-th node has been found?
        S = [s]  # Stack of nodes to explore
        R = [s]  # Visiting order
        found[s] = 1
        while S:
            u = S[-1]
            unstack = True
            for v in self.adjList[u]:
                if found[v] == 0:
                    unstack = False
                    S.append(v)
                    R.append(v)
                    found[v] = 1
                    break
            if unstack:
                S.pop(-1)
        return R

    def rec_dfs(self, s):
        """Returns the visiting order of nodes from source s through recursive dfs"""
        found = [0 for i in range(self.countNodes)]  # i-th node has been found?
        R = []  # Visiting order
        self.rec_dfs_aux(s, R, found)
        return R

    def rec_dfs_aux(self, s, R, found):
        """Auxiliary function that makes recursive calls to traverse the graph in dfs"""
        R.append(s)
        found[s] = 1
        for v in self.adj_list[s]:
            if found[v] == 0:
                self.rec_dfs_aux(v, R, found)
        return R

    def connected(self):
        """Determines whether the graph is connected or not"""
        found = [0 for i in range(self.countNodes)]  # i-th node has been found?
        Q = [0]  # Queue of nodes to discover
        found[0] = 1
        while Q:
            u = Q.pop(0)
            for v in self.adjList[u]:
                if found[v] == 0:  # Mark node v as discovered
                    Q.append(v)
                    found[v] = 1
        for i in range(len(found)):
            if found[i] == 0:  # If any node has not been discovered
                return False
        return True
