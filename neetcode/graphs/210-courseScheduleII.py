from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # create a graph of prerequisites
        graph = {courseId:set() for courseId in range(numCourses)}
        for p in prerequisites:
            requisite, next = p[1], p[0]
            graph[requisite].add(next)


        def topSort(node, visited, stackVisitedInPath):
            visited[node] = True
            stackVisitedInPath.add(node)
            for neighbor in graph[node]:
                if neighbor in stackVisitedInPath:
                    self.hasCycle = True
                if visited[neighbor] == 0:
                    topSort(neighbor, visited, stackVisitedInPath)
            stackVisitedInPath.remove(node)
            self.order.appendleft(node)

        self.hasCycle = False
        self.order = deque()
        visited = {node:False for node in graph}
        for node in graph:
            visitedInPath = set()
            if not visited[node]:
                topSort(node, visited, visitedInPath)
        if self.hasCycle:
            return []
        return list(self.order)
    

testCases = [
    (8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]), # true
    (2, [[1,0]]), # true
    (2, [[1,0],[0,1]]), # true
]

s = Solution()
for t in testCases:
    print(s.findOrder(t[0], t[1]))