from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # had to look at the solution
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision not  to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        

testCases = [
    [1,2,3],             # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
]

s = Solution()
for t in testCases:
    print(s.subsets(t))