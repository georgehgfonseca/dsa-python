class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        graph = dict()
        for i in range(len(points)):
            graph[i] = dict()
            for j in range(len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i][j] = dist
        
        # prim's algorithm
        node = 0
        connected = {node}
        heap = []
        for neighbor in graph[node]:
            heapq.heappush(heap, (graph[node][neighbor], node, neighbor))

        res = 0
        while len(connected) < len(graph):
            (weight, nei, node) = heapq.heappop(heap)
            if node in connected:
                continue
            res += weight
            connected.add(node)
            for neighbor in graph[node]:
                if neighbor not in connected:
                    heapq.heappush(heap, (graph[node][neighbor], node, neighbor))

        return res

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        # kruskal
        parent = [i for i in range(len(points))]

        # with path comprehension
        # def find(i):
        #     if parent[i] != i:
        #         parent[i] = find(parent[i])
        #     return parent[i]

        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i

        def union(i, j):
            parent[find(i)] = find(j)

        edges.sort()
        edgeCount = 0
        res = 0
        for w, u, v in edges:
            if find(u) != find(v):
                edgeCount += 1
                res += w
                union(u, v)
            if edgeCount >= len(points) - 1:
                break
            
        return res


