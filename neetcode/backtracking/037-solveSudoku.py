class Solution:
    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def getNextCell(i, j):
            if i + 1 < len(board):
                return (i + 1, j)
            return (0, j + 1)

        def getCellOptions(i, j):
            if board[i][j] != ".":
                # preassigned cell
                return {board[i][j]}

            options = set(str(i) for i in range(1, len(board) + 1))
            # check row
            for col in range(len(board[i])):
                options.discard(board[i][col])
            # check col
            for row in range(len(board)):
                options.discard(board[row][j])
            # check box
            box = (i // 3, j // 3)
            for row in range(box[0] * 3, (box[0] * 3) + 3):
                for col in range(box[1] * 3, (box[1] * 3) + 3):
                    options.discard(board[row][col])
            return options

        def dfs():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for option in getCellOptions(i, j):
                            board[i][j] = option
                            if dfs():
                                return True
                            board[i][j] = "."  # Backtrack
                        return False  # No valid option
            return True  # Solved

        dfs()


    def solveSudoku(self, board: List[List[str]]) -> None:
        def getNextCell(i, j):
            if j + 1 < len(board):
                return (i, j + 1)
            return (i + 1, 0)

        def getCellOptions(i, j):
            if board[i][j] != ".":
                # preassigned cell
                return {board[i][j]}

            options = set(str(i) for i in range(1, len(board) + 1))
            # check row
            for col in range(len(board[i])):
                options.discard(board[i][col])
            # check col
            for row in range(len(board)):
                options.discard(board[row][j])
            # check box
            box = (i // 3, j // 3)
            for row in range(box[0] * 3, (box[0] * 3) + 3):
                for col in range(box[1] * 3, (box[1] * 3) + 3):
                    options.discard(board[row][col])
            return options

        self.found = False
        def dfs(i, j):
            if self.found:
                return

            if i >= len(board):
                # found a complete solution
                self.found = True
                return

            options = getCellOptions(i, j)
            backup = board[i][j] 
            for option in options:
                if self.found:
                    break
                board[i][j] = option
                (nextI, nextJ) = getNextCell(i, j)
                dfs(nextI, nextJ)
                if not self.found:
                    board[i][j] = backup
            
        dfs(0, 0)
            

        