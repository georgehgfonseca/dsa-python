from typing import List

# premium problem available in https://leetcode.ca/all/323.html
class Solution:
    def countConnectedComponents(self, edges: List[List[int]], numNodes: int) -> int:
        # create graph from edges for faster lookup times
        graph = {node: {} for node in range(numNodes)}
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u][v] = 1
            graph[v][u] = 1
        
        # dfs to label the connected component to which each node belongs
        def dfs(node, component_id, node_component):
            node_component[node] = component_id
            for neighbor in graph[node]:
                if node_component[neighbor] == 0:
                    dfs(neighbor, component_id, node_component)

        # associates every node with a component_id >= 1
        node_component = {node: 0 for node in graph}
        component_id = 0
        for node in graph:
            if node_component[node] == 0:
                component_id += 1
                dfs(node, component_id, node_component)

        return component_id


testCases = [([[0, 1], [1, 2], [3, 4]], 5), ([[0, 1], [1, 2], [2, 3], [3, 4]], 5)]
s = Solution()
for t in testCases:
    print(s.countConnectedComponents(t[0], t[1]))
