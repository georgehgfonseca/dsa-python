from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = dict({node: set() for node in range(numCourses)})
        for prerequisite in prerequisites:
            n1, n2 = prerequisite[0], prerequisite[1]
            graph[n2].add(n1)

        # topological sort
        visited = set()
        order = []
        self.has_cycle = False

        def dfs(node, stack):
            stack.add(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in stack:
                    self.has_cycle = True
                if neighbor not in visited:
                    dfs(neighbor, stack)

            stack.remove(node)
            order.insert(0, node)


        for node in graph:
            if node not in visited:
                dfs(node, set())

        if self.has_cycle:
            return []
            
        return order


testCases = [
    (2, [[1,0],[0,1]]),
    (4, [[1,0],[2,0],[3,1],[3,2]]),
]

s = Solution()
for t in testCases:
    print(s.findOrder(t[0], t[1]))