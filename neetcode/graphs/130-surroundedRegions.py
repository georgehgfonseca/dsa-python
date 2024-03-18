from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        cells_to_keep = set()
        
        def check_neighbors(i, j):
            if i + 1 < len(board) - 1 and board[i + 1][j] == "O" and (i + 1, j) not in cells_to_keep:
                cells_to_keep.add((i + 1, j))
                check_neighbors(i + 1, j)
            if i - 1 > 0 and board[i - 1][j] == "O" and (i - 1, j) not in cells_to_keep:
                cells_to_keep.add((i - 1, j))
                check_neighbors(i - 1, j)
            if j + 1 < len(board[i]) - 1 and board[i][j + 1] == "O" and (i, j + 1) not in cells_to_keep:
                cells_to_keep.add((i, j + 1))
                check_neighbors(i, j + 1)
            if j - 1 > 0 and board[i][j - 1] == "O" and (i, j - 1) not in cells_to_keep:
                cells_to_keep.add((i, j - 1))
                check_neighbors(i, j - 1)


        for i in range(len(board)):
            for j in range(len(board[i])):
                if i in [0, len(board) - 1] or j in [0, len(board[i]) - 1]:
                    # process the borders
                    if board[i][j] == "O":
                        if (i, j) not in cells_to_keep:
                            cells_to_keep.add((i, j))
                        # check neigbors
                        check_neighbors(i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i, j) not in cells_to_keep:
                    board[i][j] = "X"





testCases = [
    [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
    [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]],
]

s = Solution()
for t in testCases:
    print(s.solve(t))