from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res



testCases = [([2, 3, 5], 8), ([2, 3, 6, 7], 7), ([7, 3, 2], 18), ([7, 3], 17), ([2, 7, 6, 3, 5, 1], 9), ([1], 1)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
