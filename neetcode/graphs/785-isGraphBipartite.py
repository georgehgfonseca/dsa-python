class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visitedColor = dict()
        self.bipartite = True

        def dfs(node, color):
            if not self.bipartite:
                return 
            if node in visitedColor:
                if visitedColor[node] != color:
                    self.bipartite = False
                return

            visitedColor[node] = color
            for neighbor in graph[node]:
                if color == 1:
                    dfs(neighbor, 2)
                else:
                    dfs(neighbor, 1)
        
        for node in range(len(graph)):
            if node not in visitedColor and self.bipartite:
                dfs(node, 1)
        return self.bipartite
