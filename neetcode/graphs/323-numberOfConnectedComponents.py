from typing import List

class Solution:
    def numConnectedComponents(self, numNodes: int, edges: List[List[int]]) -> int:
        # create graph from edge list
        graph = {node: set() for node in range(numNodes)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        # run dfs and label all found nodes with same label
        nodeVisited = {node:0 for node in graph}
        
        def dfs(node, label):
            nodeVisited[node] = label
            for neighbor in graph[node]:
                if nodeVisited[neighbor] == 0:
                    dfs(neighbor, label)

        label = 0
        for node in graph:
            if nodeVisited[node] == 0:
                label += 1
                dfs(node, label)

        numIsolatedNodes = 0
        for node in graph:
            if nodeVisited[node] == 0:
                numIsolatedNodes += 1
            
        return label + numIsolatedNodes


testCases = [
    (5, [[0, 1], [1, 2], [3, 4]]), # 2
]

s = Solution()
for t in testCases:
    print(s.numConnectedComponents(t[0], t[1]))