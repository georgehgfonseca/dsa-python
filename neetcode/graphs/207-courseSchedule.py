from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # copied solution from neetcode:
        # # dfs
        # preMap = {i: [] for i in range(numCourses)}

        # # map each course to : prereq list
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)

        # visiting = set()

        # def dfs(crs):
        #     if crs in visiting:
        #         return False
        #     if preMap[crs] == []:
        #         return True

        #     visiting.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visiting.remove(crs)
        #     preMap[crs] = []
        #     return True

        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True
    
        # create a graph of prerequisites
        graph = {}
        for p in prerequisites:
            requisite, next = p[0], p[1]
            if requisite not in graph:
                graph[requisite] = set()
            if next not in graph:
                graph[next] = set()
            graph[requisite].add(next)

        self.hasCycle = False
        def dfs(node, visited, current_path):
            visited[node] = True
            current_path[node] = True

            for neighbor in graph[node]:
                if current_path[neighbor]:
                    self.hasCycle = True
                    break
                elif not visited[neighbor]:
                    dfs(neighbor, visited, current_path)

            current_path[node] = False

        for node in graph:
            visited = {node:False for node in graph}
            current_path = {node:False for node in graph}
            dfs(node, visited, current_path)
            if self.hasCycle:
                return False
        return True
    

testCases = [
    (8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]), # true
    (2, [[1,0]]), # true
    (2, [[1,0],[0,1]]), # false
]

s = Solution()
for t in testCases:
    print(s.canFinish(t[0], t[1]))