from typing import List
from collections import deque

class Solution:
    def graphValidTree(self, numNodes: int, edges: List[List[int]]) -> bool:
        if numNodes - 1 != len(edges):
            # it is not connected or not acyclic
            return False
        
        # create a graph for faster lookup times
        graph = {nodeId: set() for nodeId in range(numNodes)}
        for edge in edges:
            source, sink = edge[0], edge[1]
            graph[source].add(sink)
            graph[sink].add(source)

        # dfs to check if graph is connected (having n-1 edges means it is also acyclic)
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in graph:
            dfs(node)
            # only have to look the 1st node
            break

        if len(visited) != numNodes:
            return False
        
        return True

testCases = [
    (5, [[0,1], [0,2], [0,3], [1,4]]), # true
]

s = Solution()
for t in testCases:
    print(s.graphValidTree(t[0], t[1]))