from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def aux(currIdx, currSubset):
            print(currSubset)
            if currIdx >= len(nums):
                ans.append(currSubset)
                return
            
            aux(currIdx + 1, currSubset.copy())
            aux(currIdx + 1, currSubset.copy() + [nums[currIdx]])

        aux(0, [])            
        return ans


testCases = [
    [1,2,3],             # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
]

s = Solution()
for t in testCases:
    print(s.subsets(t))