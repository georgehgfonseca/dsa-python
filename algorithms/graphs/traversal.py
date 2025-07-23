import heapq
from typing import Set, Dict, List
from collections import deque

class Solution:
    def bfs(self, graph: Dict[int, Set[int]], source: int) -> List[int]:
        queue = deque([source])
        order = [source]
        visited = {source}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    order.append(neighbor)
        return order

    def dfs(self, graph: Dict[int, Set[int]], source: int) -> List[int]:
        visited = {source}
        order = [source]

        def aux(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    order.append(neighbor)
                    aux(neighbor)

        aux(source)
        return order

    def hasCycle(self, graph: Dict[int, Set[int]], source: int) -> List[int]:
        visited = {source}
        stack = {source}
        self.cycle = False

        def aux(node):
            for neighbor in graph[node]:
                if neighbor in stack:
                    self.cycle = True
                    break
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.add(neighbor)
                    aux(neighbor)
                    stack.discard(neighbor)

        aux(source)
        return self.cycle


s = Solution()
print(s.dfs({0: {1, 2}, 1: {0, 3, 4}, 2: {0, 5, 6}, 3: {1}, 4: {1}, 5: {2}, 6: {2}}, 0))
print(s.hasCycle({0: {1, 2}, 1: {3}, 2: {3}, 3: {}}, 0))