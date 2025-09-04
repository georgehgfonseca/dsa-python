class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dfs(level, idx):
            if level >= len(triangle):
                return 0

            # can go either left or right on the next level
            return min(triangle[level][idx] + dfs(level + 1, idx), triangle[level][idx] + dfs(level + 1, idx + 1))
        
        return dfs(0, 0)
