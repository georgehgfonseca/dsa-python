class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # run dijkstra from (0, 0) to (m-1, n-1) distance is the absolute diff between height of a cell and another
        M, N = len(heights), len(heights[0])
        diff = {(row, col): float("inf") for row in range(M) for col in range(N)}
        visited = set()
        start, target = (0, 0), (M - 1, N - 1)
        diff[start] = 0
        heap = [(0, start)]
        
        while heap:
            diffNode, node = heapq.heappop(heap)
            if node == target:
                break
            visited.add(node)
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for offset in moves:
                neighbor = (node[0] + offset[0], node[1] + offset[1])
                if neighbor[0] >= M or neighbor[1] >= N or neighbor[0] < 0 or neighbor[1] < 0 or neighbor in visited:
                    continue
                
                if diff[neighbor] > max(diff[node], abs(heights[node[0]][node[1]] - heights[neighbor[0]][neighbor[1]])):
                     diff[neighbor] = max(diff[node], abs(heights[node[0]][node[1]] - heights[neighbor[0]][neighbor[1]]))
                     heapq.heappush(heap, (diff[neighbor], neighbor))
        
        return diff[target]