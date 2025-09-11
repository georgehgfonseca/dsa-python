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