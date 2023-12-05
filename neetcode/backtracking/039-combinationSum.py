from typing import List

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # while node
        # expand the search to the nodes higher or equals than node that 

        res = []
        curr = []
        def dfs(i, curr, curr_sum):
            if i != -1:
                curr.append(candidates[i])
                curr_sum += candidates[i]
                if curr_sum >= target:
                    if curr_sum == target:
                        res.append(curr.copy())
                    return
            else:
                i += 1
            
            # expand the search
            for j in range(i, len(candidates)):
                dfs(j, curr.copy(), curr_sum)

        candidates.sort()
        dfs(-1, curr, 0)

        return res
        

testCases = [
    ([2,3,6,7], 7),  # [[2,2,3], [7]]
    ([2,3,5], 8),    # [[2,2,2,2], [2,3,3], [3,5]]
]

s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))