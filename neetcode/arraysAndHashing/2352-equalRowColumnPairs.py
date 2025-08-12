class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            currRow = grid[i]
            for i2 in range(len(grid)):
                isPair = True
                for j in range(len(grid[i])):
                    if currRow[j] != grid[j][i2]:
                        isPair = False
                        break
                if isPair:
                    res += 1
        return res
        