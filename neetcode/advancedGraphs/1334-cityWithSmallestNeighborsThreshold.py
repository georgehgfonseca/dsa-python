class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # run dijkstra having each node as source
        def dijkstra(graph, source):
            visited = set()
            dist = {node: float("inf") for node in graph}
            dist[source] = 0
            heap = [(0, source)]
            while heap:
                nodeDist, node = heapq.heappop(heap)
                visited.add(node)
                for neighbor in graph[node]:
                    inThreshold = dist[node] + graph[node][neighbor] <= distanceThreshold
                    if dist[neighbor] > dist[node] + graph[node][neighbor] and neighbor not in visited and inThreshold:
                        dist[neighbor] = dist[node] + graph[node][neighbor]
                        heapq.heappush(heap, (dist[neighbor], neighbor))
            visited.remove(source)
            return visited

        graph = {node: dict() for node in range(n)}
        for s, t, w in edges:
            graph[s][t] = w
            graph[t][s] = w
        print(graph)
        
        # return the node with least neighbors in threshold (or largest index in case of ties)
        nodeMinNeiInThreshold = 0
        minNeiInThreshold = float("inf")
        for node in graph:
            neighborsInThreshold = dijkstra(graph, node)
            if len(neighborsInThreshold) <= minNeiInThreshold:
                minNeiInThreshold = len(neighborsInThreshold)
                nodeMinNeiInThreshold = node
        return nodeMinNeiInThreshold