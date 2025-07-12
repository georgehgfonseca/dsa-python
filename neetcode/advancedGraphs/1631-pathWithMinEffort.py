import heapq

class Solution:


    def get_neighbor_cells(self, i, j, heights):
        neighbors = dict()
        if i - 1 >= 0:
            neighbors[(i - 1, j)] = abs(heights[i][j] - heights[i - 1][j])
        if j - 1 >= 0:
            neighbors[(i, j - 1)] = abs(heights[i][j] - heights[i][j - 1])
        if i + 1 < len(heights):
            neighbors[(i + 1, j)] = abs(heights[i][j] - heights[i + 1][j])
        if j + 1 < len(heights[i]):
            neighbors[(i, j + 1)] = abs(heights[i][j] - heights[i][j + 1])
        return neighbors
    
    def dijkstra(self, graph, start, end):
        dist = {node: float("inf") for node in graph}
        prev = {node: None for node in graph}
        # optmize with heapq
        queue = [(0, start)]
        dist[start] = 0
        while queue:
            (_, node) = heapq.heappop(queue)
            for neighbor in graph[node]:
                if dist[neighbor] > max(dist[node], graph[node][neighbor]):
                    dist[neighbor] = max(dist[node], graph[node][neighbor])
                    prev[neighbor] = node
                    heapq.heappush(queue, (dist[neighbor], neighbor))
        return dist, prev


    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # create a graph of cells and effort to neighboring cells
        graph = dict()
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                graph[(i, j)] = self.get_neighbor_cells(i, j, heights)
        
        # compute dijkstra's for shortest path
        start, end = (0, 0), (len(heights) - 1, len(heights[0]) - 1)
        dist, prev = self.dijkstra(graph, start, end)

        return dist[end]

