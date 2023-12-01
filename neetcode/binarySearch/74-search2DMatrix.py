from typing import List

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        start = 0
        end = (n_rows * n_cols) - 1

        while start <= end:
            mid = (start + end) // 2
            i, j = mid // n_cols, mid % n_cols
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False

testCases = [
    ([[ 1, 3, 5, 7],
      [10,11,16,20],
      [23,30,34,60]], 3),   # True
      # n_rows: 3
      # n_cols: 4
      # mid:    10 -> 2,2
    ([[ 1, 3, 5, 7],
      [10,11,16,20],
      [23,30,34,60]], 13),   # False
]

s = Solution()
for t in testCases:
    print(s.searchMatrix(t[0], t[1]))