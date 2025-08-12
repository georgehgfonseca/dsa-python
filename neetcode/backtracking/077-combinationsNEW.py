class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr[:])
                return 
            
            for j in range(i, n + 1):
                dfs(j + 1, curr + [j])
        
        dfs(1, [])
        return res