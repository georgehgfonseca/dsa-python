from typing import List

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for col in range(n + 1)] for row in range(m + 1)]

        # in the last row there is only one way to move to the target (forward)
        for col in range(n):
            grid[m-1][col] = 1
        # in the last col there is only one way to move to the target (down)
        for row in range(m):
            grid[row][n-1] = 1

        # bottom-up approach until reach the starting position
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                # ways in (row, cols) = sum of ways in right and down cells
                grid[row][col] = grid[row+1][col] + grid[row][col+1]

        return grid[0][0]


#      0  1  2  3  4  5  6  7
#    -----------------------
# 0: | 0  0  0  0  0  0  1  0
# 1: | 0  0  0  0  0  0  1  0
# 2: | 1  1  1  1  1  1  1  0
# 3: | 0  0  0  0  0  0  0  0

# m: 3
# n: 7

testCases = [
    (3, 7) # 28
]

s = Solution()
for t in testCases:
    print(s.uniquePaths(t[0], t[1]))