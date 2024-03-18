from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1, curr.copy())
            curr.pop()
            dfs(i+1, curr.copy())

        curr = []
        dfs(0, curr)

        return res
        

testCases = [
    [1,2,3],             # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
]

s = Solution()
for t in testCases:
    print(s.subsets(t))