class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        self.res = 0
        visited = {node: 0 for node in range(len(isConnected))}
        graph = {node: set() for node in range(len(isConnected))}
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j]:
                    graph[i].add(j)

        def dfs(node):
            visited[node] = self.res
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    dfs(neighbor)

        for node in graph:
            if visited[node] == 0:
                self.res += 1
                dfs(node)
        return self.res
        