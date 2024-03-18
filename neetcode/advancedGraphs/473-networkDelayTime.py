from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = dict({node: dict() for node in range(1, n + 1)})
        for (source, sink, weight) in times:
            graph[source][sink] = weight

        # dijkstra's shortest path algoithm
        def dijkstra(s):
            dist = {node: float("inf") for node in graph}
            pred = {node: None for node in graph}

            dist[s] = 0
            nodes_to_process = [(0, s)]
            while nodes_to_process:
                (_, u) = heapq.heappop(nodes_to_process)
                for neighbor in graph[u]:
                    if dist[neighbor] > dist[u] + graph[u][neighbor]:
                        dist[neighbor] = dist[u] + graph[u][neighbor]
                        pred[neighbor] = u
                        heapq.heappush(nodes_to_process, (dist[neighbor], neighbor))
            
            return dist, pred

        dist, pred = dijkstra(k)

        # get largest dist as answer
        res = -1
        for node in dist:
            res = max(res, dist[node])

        if res == float("inf"):
            return -1

        return res


testCases = [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2), # 2
]

s = Solution()
for t in testCases:
    print(s.networkDelayTime(t[0], t[1], t[2]))
