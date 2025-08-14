class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visitedSet = dict()
        self.bipartite = True

        def dfs(node, set):
            if not self.bipartite:
                return 
            if node in visitedSet:
                if visitedSet[node] != set:
                    self.bipartite = False
                return

            visitedSet[node] = set
            for neighbor in graph[node]:
                if set == 1:
                    dfs(neighbor, 2)
                else:
                    dfs(neighbor, 1)
        
        for node in range(len(graph)):
            if node not in visitedSet and self.bipartite:
                dfs(node, 1)
        return self.bipartite
