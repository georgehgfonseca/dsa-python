from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # preprocess times into a graph
        graph = {node: {} for node in range(1, n + 1)}
        for time in times:
            u, v, w = time[0], time[1], time[2]
            graph[u][v] = w

        # compute distances using Dijkstra's algorithm
        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0
        heap = []
        heapq.heappush(heap, (0, k))
        while heap:
            dist_u, u = heapq.heappop(heap)
            for v in graph[u]:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    heapq.heappush(heap, (dist[v], v))

        # get longest distance
        longest_dist = -1
        for node in dist:
            longest_dist = max(longest_dist, dist[node])

        if longest_dist == float("inf"):
            return -1
        return longest_dist



testCases = [([[2,1,1],[2,3,1],[3,4,1]], 4, 2), ([[1,2,1]], 2, 1)]
s = Solution()
for t in testCases:
    print(s.networkDelayTime(t[0], t[1], t[2]))
