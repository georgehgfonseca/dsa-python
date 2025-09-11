# based on https://www.youtube.com/watch?v=Ti5vfu9arXQ

# good farm land: find the largest square of ones
from typing import List

class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = dict()
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            out_of_bounds = i >= len(matrix) or j >= len(matrix[i])
            if out_of_bounds or matrix[i][j] == "0":
                return 0
            
            cache[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            return cache[(i, j)]
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, dfs(i, j))

        return res * res


testCases = [([[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 0]], 9)]
s = Solution()
for t in testCases:
    print(s.maximalSquare(t[0]))
    # assert s.largestSquare(t[0]) == t[1], "Wrong answer"


