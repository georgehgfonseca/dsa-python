from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # create a graph of cells and their neighbors (only 1s)
        graph = dict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    graph[(i,j)] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    if i < len(grid) - 1 and grid[i+1][j] == "1":
                        # edge between (i,j) and (i+1,j)
                        graph[(i,j)].add((i+1,j)) 
                        graph[(i+1,j)].add((i,j)) 
                    if i > 0 and grid[i-1][j] == "1":
                        # edge between (i,j) and (i-1,j)
                        graph[(i,j)].add((i-1,j)) 
                        graph[(i-1,j)].add((i,j)) 
                    if j < len(grid[i]) - 1 and grid[i][j+1] == "1":
                        # edge between (i,j) and (i,j+1)
                        graph[(i,j)].add((i,j+1)) 
                        graph[(i,j+1)].add((i,j)) 
                    if j > 0 and grid[i][j-1] == "1":
                        # edge between (i,j) and (i,j-1)
                        graph[(i,j)].add((i,j-1)) 
                        graph[(i,j-1)].add((i,j)) 
        
        # count the connected components in this graph
        node_component = {node: 0 for node in graph}
        def dfs(node, component):
            node_component[node] = component
            for neighbor in graph[node]:
                if node_component[neighbor] == 0:
                    dfs(neighbor, component)

        component = 0
        for node in graph:
            if node_component[node] == 0:
                component += 1
                dfs(node, component)
        
        return component
        

testCases = [
 [["1","1","1","1","0"], # 1
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
],
 [["1","1","0","0","0"], # 3
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]]

s = Solution()
for t in testCases:
    print(s.numIslands(t))