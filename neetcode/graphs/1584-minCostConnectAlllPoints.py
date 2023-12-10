from typing import List
import heapq
import math

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create a graph (adj_matrix) of costs
        graph = [[None for i in range(len(points))] for j in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x_i, y_i = points[i][0], points[i][1]
                x_j, y_j = points[j][0], points[j][1]
                dist = abs(x_i - x_j) + abs(y_i - y_j)
                graph[i][j] = dist
                graph[j][i] = dist

        # find the minimum cost to connect all the points (Prim's algorithm)
        res = 0
        connectedNodes = set()
        heap = [(0, 0)]
        while len(connectedNodes) < len(graph):
            cost, node = heapq.heappop(heap)
            if node in connectedNodes:
                continue
            res += cost
            connectedNodes.add(node)
            for neighbor in range(len(graph[node])):
                if neighbor not in connectedNodes and node != neighbor:
                    heapq.heappush(heap, (graph[node][neighbor], neighbor))
        
        return res


testCases = [
    [[0,0],[2,2],[3,10],[5,2],[7,0]]
]

s = Solution()
for t in testCases:
    print(s.minCostConnectPoints(t))