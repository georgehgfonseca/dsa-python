class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {(row, col): 0 for row in range(len(grid)) for col in range(len(grid[row]))}
        self.res = 0

        def dfs(row, col):
            if (row, col) not in visited or visited[(row, col)] != 0 or grid[row][col] == "0":
                return
            visited[(row, col)] = self.res

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if visited[(row, col)] == 0 and grid[row][col] == "1":
                    self.res += 1
                    dfs(row, col)
        
        return self.res
            
