from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # verify if corresponding courses graph is acyclic (DAG)
        # create a prerequisite graph
        # can do bellman-ford, but expensive O(n * m)
        # detect cycle - dfs
        # prerequisites         = [(1, 0), (2, 0), (2, 1)]  true (no cycle)
        # graph                 = {0: {1, 2}, 2: {1}}
        # stack                 = {}
        # visited               = {0, 1, 2}
        graph = {i: set() for i in range(numCourses)}
        for prereq in prerequisites:
            before = prereq[1]
            after = prereq[0]
            graph[before].add(after)


        def check_cycle(start, stack):
            for neighbor in graph[start]:
                if neighbor in stack:
                    self.has_cycle = True
                    return
                if neighbor not in visited:
                    visited.add(neighbor)
                    newStack = stack.copy()
                    newStack.add(neighbor)
                    check_cycle(neighbor, newStack)

        
        visited = set()
        self.has_cycle = False
        for node in graph:
            stack = {node}
            if node not in visited: 
                check_cycle(node, stack)
                if self.has_cycle:
                    return False
        return True

testCases = [
    (4, [[1,0],[2,0],[3,1],[3,2]]), # true
    (2, [[1,0],[0,1]]), # false
    (8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]), # true
    (2, [[1,0]]), # true
]

s = Solution()
for t in testCases:
    print(s.canFinish(t[0], t[1]))