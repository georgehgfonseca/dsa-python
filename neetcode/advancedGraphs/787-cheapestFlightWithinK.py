from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for source, sink, price in flights:
            graph[source][sink] = price
        
        queue = [(0, src, -1)]
        # minimum current distance with n stops
        dist = [[float("inf") for _ in range(k + 2)] for i in range(n)] # (cost, hops)
        dist[src][0] = 0

        while queue:
            distNode, node, stops = heapq.heappop(queue)
            if node == dst:
                return distNode
            if stops == k or dist[node][stops + 1] < distNode:
                continue

            for neighbor in graph[node]:
                nextStops = stops + 1
                if dist[neighbor][nextStops + 1] > distNode + graph[node][neighbor]:
                    dist[neighbor][nextStops + 1] = distNode + graph[node][neighbor]
                    heapq.heappush(queue, (dist[neighbor][nextStops + 1], neighbor, nextStops))
        
        return -1
        
    def findCheapestPriceBF(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0

        for _ in range(k + 1):
            tmpDist = dist.copy()
            for source, sink, weight in flights:
                if dist[source] == float("inf"):
                    continue

                if tmpDist[sink] > dist[source] + weight:
                    tmpDist[sink] = dist[source] + weight
            
            dist = tmpDist
        
        return -1 if dist[dst] == float("inf") else dist[dst]
        
    
s = Solution()
print(s.findCheapestPrice(5, [[0, 1, 5], [0, 3, 2], [1, 4, 1], [1, 2, 5], [3, 1, 2], [4, 2, 1]], 0, 2, 2))