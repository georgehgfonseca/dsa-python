import heapq


class WeightedGraph:
    def __init__(self, countNodes, countEdges=0):
        self.countNodes = countNodes
        self.countEdges = countEdges
        self.adjMatrix = [[0 for _ in range(countNodes)] for _ in range(countNodes)]
        # self.adjList = [[] for i in range(countNodes)]
        self.adjList = {}
        for i in range(countNodes):
            self.adjList[i] = []

    def addEdge(self, u, v, w):
        if u < self.countNodes and u >= 0 and v < self.countNodes and v >= 0 and w > 0:
            self.adjMatrix[u][v] = w
            self.adjList[u].append((v, w))
            self.countEdges += 1

    def addUndirectedEdge(self, u, v, w):
        if u < self.countNodes and u >= 0 and v < self.countNodes and v >= 0 and w > 0:
            self.adjMatrix[u][v] = w
            self.adjMatrix[v][u] = w
            self.adjList[u].append((v, w))
            self.adjList[v].append((u, w))
            self.countEdges += 2

    def toString(self):
        res = ""
        for u in range(len(self.adjList)):
            res += str(u) + ": "
            for (v, w) in self.adjList[u]:
                res += "(" + str(v) + ", " + str(w) + ") "
            res += "\n"
        return res

    def bfs(self, s):
        """Returns the visiting order of nodes from source s through bfs"""
        found = [0 for i in range(self.countNodes)]  # i-th node has been found?
        Q = [s]  # Queue of nodes to explore
        R = [s]  # Visiting order
        found[s] = 1
        while Q:
            u = Q.pop(0)
            for (v, w) in self.adjList[u]:
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
            for (v, w) in self.adjList[u]:
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
        for (v, w) in self.adj_list[s]:
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
            for (v, w) in self.adjList[u]:
                if found[v] == 0:  # Mark node v as discovered
                    Q.append(v)
                    found[v] = 1
        for i in range(len(found)):
            if found[i] == 0:  # If any node has not been discovered
                return False
        return True

    def dijkstra_pq(self, s, t):
        """Returns the shortest path from s to t through dijkstra's algorithm using priority queue
        Based on: https://www.geeksforgeeks.org/implement-min-heap-using-stl/
        and https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/"""
        dist = [float("inf") for _ in range(self.countNodes)]  # Distance from s
        pred = [None for _ in range(self.countNodes)]  # Predecessor in shortest path from s
        pq = []
        heapq.heapify(pq)  # Empty priority queue
        q = [1 for _ in range(self.countNodes)]  # Node has to be processed? (0/1)
        nodesCount = 0  # Counter of processed nodes
        dist[s] = 0
        heapq.heappush(pq, [0, s])
        while heapq:
            [min_dist, u] = heapq.heappop(pq)
            if u == t:  # For single sink shortest path algorithm can be interrupted here!
                break
            q[u] = 0
            nodesCount += 1
            for (v, w) in self.adjList[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    heapq.heappush(pq, [dist[v], v])
        return dist, pred

    def nearestNeighbor(self):
        """Returns an Hamiltonian cycle (visits all nodes) based on the nearest neighbor greedy heuristic
        Assumes a complete graph as input"""
        u = 0  # Initial node
        C = []  # Hamiltonian cycle
        cost = 0  # Cost of the returned hamiltonian cycle
        Q = [v for v in range(self.countNodes)]  # Node to visit
        Q.remove(u)
        # It is easier (and faster) to work with adjacency matrix in this algorithm
        while Q:
            # Nearest non-visited neighbor of u (v)
            minDist = float("inf")
            minV = Q[0]
            for v in Q:
                if self.adjMatrix[u][v] != 0 and self.adjMatrix[u][v] < minDist:
                    minDist = self.adjMatrix[u][v]
                    minV = v
            v = minV
            C.append(v)
            cost += minDist
            Q.remove(v)
            u = v
        C.append(C[0])
        return C, cost
