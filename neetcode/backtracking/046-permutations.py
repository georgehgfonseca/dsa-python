from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        # using sets to speedup belonging checks
        res = []

        def dfs(i, curr, curr_set):
            curr.append(nums[i])
            curr_set.add(nums[i])
            if len(curr) == len(nums):
                res.append(curr)
                return
            for j in range(len(nums)):
                if nums[j] not in curr_set:
                    dfs(j, curr.copy(), curr_set.copy())

        for i in range(len(nums)):
            dfs(i, [], set())
        return res
        
        # res = []

        # def dfs(i, curr):
        #     curr.append(nums[i])
        #     if len(curr) == len(nums):
        #         res.append(curr)
        #         return
        #     for j in range(len(nums)):
        #         if nums[j] not in curr:
        #             dfs(j, curr.copy())

        # for i in range(len(nums)):
        #     dfs(i, [])
        # return res
        

testCases = [
    [1,2,3],  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    [0,1],    # [[0,1],[1,0]]
]

s = Solution()
for t in testCases:
    print(s.permute(t))