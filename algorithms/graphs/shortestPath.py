import heapq
from typing import List, Tuple, Dict

class Solution:
    def dijkstra(self, n: int, edges: List[Tuple[int, int, int]], src: int) -> Dict[int, int]:
        graph = {node: dict() for node in range(n)}
        for (source, sink, weight) in edges:
            graph[source][sink] = weight

        dist = {node: float("inf") for node in graph}
        dist[src] = 0
        queue = [(0, src)]
        while queue:
            (_, node) = heapq.heappop(queue)
            for nei in graph[node]:
                if dist[nei] > dist[node] + graph[node][nei]:
                    dist[nei] = dist[node] + graph[node][nei]
                    heapq.heappush(queue, (dist[nei], nei))

        for node in graph:
            dist[node] = -1 if dist[node] == float("inf") else dist[node]
        return dist

s = Solution()
print(s.dijkstra(5, [[0, 1, 5], [1, 2, 4], [2, 3, 3], [3, 4, 2], [4, 0, 1], [2, 4, 1]], 0))