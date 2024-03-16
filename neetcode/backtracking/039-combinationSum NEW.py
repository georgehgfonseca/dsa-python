from typing import List

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def helper(curr_idx, curr_path, curr_sum):
            curr_path.append(candidates[curr_idx])
            curr_sum += candidates[curr_idx]
            
            if curr_sum > target:
                return
            
            if curr_sum == target:
                res.append(curr_path)
                return

            for i in range(curr_idx, len(candidates)):
                helper(i, curr_path[:], curr_sum)
        
        for i in range(len(candidates)):
            helper(i, [], 0)
        return res

        

testCases = [
    ([2,3,6,7], 7),  # [[2,2,3], [7]]
    ([2,3,5], 8),    # [[2,2,2,2], [2,3,3], [3,5]]
]

s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))