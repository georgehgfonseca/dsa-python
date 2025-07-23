from typing import List, Tuple
import heapq
from collections import defaultdict

class Solution:
    def kruskal(self, n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
        edges.sort(key=lambda x: x[2])
        parent = {i: i for i in range(n)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)
            
        mst = []
        for edge in edges:
            if find(edge[0]) != find(edge[1]):
                union(edge[0], edge[1])
                mst.append(edge)
                if len(mst) == n - 1:
                    break
        return mst
    
    def prim(self, n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
        # graph = {i: dict() for i in range(n)}
        graph = defaultdict(dict)
        for (source, sink, weight) in edges:
            graph[source][sink] = weight 
            graph[sink][source] = weight

        mst = []
        connected = {0}
        edgeHeap = []
        for neighbor in graph[0]:
            heapq.heappush(edgeHeap, (graph[0][neighbor], 0, neighbor))

        while edgeHeap:
            (weight, source, sink) = heapq.heappop(edgeHeap)
            if sink not in connected:
                mst.append((source, sink, weight))
                connected.add(sink)
                if len(connected) == n:
                    break
                
                for neighbor in graph[sink]:
                    if neighbor not in connected:
                        heapq.heappush(edgeHeap, (graph[sink][neighbor], sink, neighbor))

        return mst


s = Solution()
print(s.prim(5, [[0, 1, 5], [1, 2, 4], [2, 3, 3], [3, 4, 2], [4, 0, 1], [2, 4, 1]]))