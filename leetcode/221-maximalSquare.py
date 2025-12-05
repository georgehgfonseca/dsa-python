# based on https://www.youtube.com/watch?v=Ti5vfu9arXQ

# good farm land: find the largest square of ones
from typing import List
from functools import cache


class Solution:
    def maximalSquare(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            out_of_bounds = i >= len(matrix) or j >= len(matrix[i])
            if out_of_bounds or matrix[i][j] == "0":
                return 0

            return 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, dfs(i, j))

        return res * res


testCases = [
    (
        [
            ["0", "1", "1", "1"],
            ["0", "1", "1", "1"],
            ["0", "1", "1", "1"],
            ["0", "1", "0", "0"],
        ],
        9,
    ),
    ([["0"]], 0),
    ([["1"]], 1),
    ([["1", "0"], ["0", "1"]], 1),
]
s = Solution()
for t in testCases:
    print(s.maximalSquare(t[0]))
    assert s.maximalSquare(t[0]) == t[1], "Wrong answer"
