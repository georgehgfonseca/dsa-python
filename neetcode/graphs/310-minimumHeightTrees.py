from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # remove degree 1 nodes until only 2 or 1 remain
        graph = {i: set() for i in range(n)}
        for source, sink in edges:
            graph[source].add(sink)
            graph[sink].add(source)
        
        while len(graph) > 2:
            toRemove = []
            for node in graph:
                if len(graph[node]) == 1:
                    toRemove.append(node)
            for node in toRemove:
                graph.pop(node)
            for node in graph:
                for removeNode in toRemove:
                    graph[node].discard(removeNode)
        return [node for node in graph]



    def findMinHeightTreesTL(self, n: int, edges: List[List[int]]) -> List[int]:
        # bfs on each node and count the height
        graph = {i: set() for i in range(n)}
        for source, sink in edges:
            graph[source].add(sink)
            graph[sink].add(source)
        

        def bfs(start, prevMinHeight) -> int:
            depth = [-1 for _ in graph]
            queue = deque([start])
            depth[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if depth[neighbor] == -1:
                        queue.append(neighbor)
                        depth[neighbor] = depth[node] + 1

                        # prune - no need to check further
                        if depth[neighbor] > prevMinHeight:
                            return float("inf")
            return max(depth)

        minHeight = float("inf")
        minHeightNodes = []
        for node in graph:
            # run bfs
            nodeHeight = bfs(node, minHeight)
            if nodeHeight < minHeight:
                minHeight = nodeHeight
                minHeightNodes = [node]
            elif nodeHeight == minHeight:
                minHeightNodes.append(node)

        return minHeightNodes
        