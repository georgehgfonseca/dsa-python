from typing import List

class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = set()
        def helper(i, curr):
            if i >= len(nums):
                res.add(tuple(curr.copy()))
                return
            
            curr.append(nums[i])
            helper(i+1, curr.copy())
            curr.pop()
            helper(i+1, curr.copy())

        helper(0, [])

        # decode tuples to lists
        decoded = [list(t) for t in res]
        return decoded
        

testCases = [
    
    # i: 3
    # curr: [1,2,2]
    [1,2,2],             # [[],[1],[1,2],[1,2,2],[2],[2,2]]
]

s = Solution()
for t in testCases:
    print(s.subsetsWithDup(t))
