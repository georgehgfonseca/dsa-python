from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(remaining, curr):
            if not remaining:
                res.append(curr[:])
                return

            for i in range(len(remaining)):
                nextRemaining = remaining[:]
                val = nextRemaining.pop(i)
                dfs(nextRemaining, curr + [val])
        
        dfs(nums, [])
        return res
        