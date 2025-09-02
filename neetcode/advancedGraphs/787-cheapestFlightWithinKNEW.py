class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra but control the number of hops on an additional structure
        # I can flight to a city with X cost and Y hops (array of distHops?)
        graph = {node: dict() for node in range(n)}
        for u, v, w in flights:
            graph[u][v] = w

        distHops = {node: [float("inf") for _ in range(k + 2)] for node in graph}
        heap = [(0, 0, src)] # (dist, hops, node)
        distHops[src][0] = 0

        while heap:
            (distNode, hopsNode, node) = heapq.heappop(heap)
            if node == dst:
                return distNode
            if hopsNode > k:
                continue
            for neighbor in graph[node]:
                if distHops[neighbor][hopsNode + 1] > distHops[node][hopsNode] + graph[node][neighbor]:
                    distHops[neighbor][hopsNode + 1] = distHops[node][hopsNode] + graph[node][neighbor]
                    heapq.heappush(heap, (distHops[neighbor][hopsNode + 1], hopsNode + 1, neighbor))

        return -1




        