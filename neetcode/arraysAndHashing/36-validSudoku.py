from typing import List
import heapq

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # assumes board is 9x9
        n = len(board)

        # validate rows
        for row in range(n):
            appear_in_col = set()
            for col in range(n):
                val = board[row][col]
                if val == ".":
                    continue
                if val in appear_in_col:
                    return False
                appear_in_col.add(val)

        # validate cols
        for col in range(n):
            appear_in_col = set()
            for row in range(n):
                val = board[row][col]
                if val == ".":
                    continue
                if val in appear_in_col:
                    return False
                appear_in_col.add(val)

        # validate boxes
        boxes = [((0,3), (0,3)), ((0,3), (3,6)), ((0,3), (6,9)),
                 ((3,6), (0,3)), ((3,6), (3,6)), ((3,6), (6,9)),
                 ((6,9), (0,3)), ((6,9), (3,6)), ((6,9), (6,9))]
        for box in boxes:
            min_row, max_row = box[0]
            min_col, max_col = box[1]
            appear_in_box = set()
            for row in range(min_row, max_row):
                for col in range(min_col, max_col):
                    val = board[row][col]
                    if val == ".":
                        continue
                    if val in appear_in_box:
                        return False
                    appear_in_box.add(val)
        
        return True


test_cases = [
    [[".",".",".",".","5",".",".","1","."],
     [".","4",".","3",".",".",".",".","."],
     [".",".",".",".",".","3",".",".","1"],
     ["8",".",".",".",".",".",".","2","."],
     [".",".","2",".","7",".",".",".","."],
     [".","1","5",".",".",".",".",".","."],
     [".",".",".",".",".","2",".",".","."],
     [".","2",".","9",".",".",".",".","."],
     [".",".","4",".",".",".",".",".","."]], # False

    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]],   # True

    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]]   # False

s = Solution()
for t in test_cases:
    print(s.isValidSudoku(t))

