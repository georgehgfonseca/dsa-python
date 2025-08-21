class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node: dict() for node in range(1, n + 1)}
        for (s, t, w) in times:
            graph[s][t] = w
        
        dist = {node: float("inf") for node in graph}
        visited = set()
        dist[k] = 0
        heap = [(0, k)]
        while heap:
            (nodeDist, node) = heapq.heappop(heap)
            visited.add(node)
            for neighbor in graph[node]:
                if dist[neighbor] > dist[node] + graph[node][neighbor] and neighbor not in visited:
                    dist[neighbor] = dist[node] + graph[node][neighbor]
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        
        if len(visited) < n:
            return -1
        
        maxDist = 0
        for node in dist:
            maxDist = max(maxDist, dist[node])
        return maxDist