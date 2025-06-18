from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(len(board)):
            col_nums = set()
            for row in range(len(board)):
                cell = board[col][row]
                if cell != "." and cell in col_nums:
                    return False
                else:
                    col_nums.add(cell) 
        for col in range(len(board)):
            col_nums = set()
            for row in range(len(board)):
                cell = board[row][col]
                if cell != "." and cell in col_nums:
                    return False
                else:
                    col_nums.add(cell)
        block_size = 3
        row_blocks = int(len(board) / block_size)
        col_blocks = int(len(board) / block_size)
        for row_block in range(row_blocks):
            for col_block in range(col_blocks):
                block_nums = set()
                for row in range(row_block * block_size, row_block * block_size + block_size):
                    for col in range(col_block * block_size, col_block * block_size + block_size):
                        cell = board[row][col]
                        if cell != "." and cell in block_nums:
                            return False
                        else:
                            block_nums.add(cell)
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

