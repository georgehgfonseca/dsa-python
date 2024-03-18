from typing import List

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def helper(curr_idx, curr_path, curr_sum):
            curr_path.append(candidates[curr_idx])
            curr_sum += candidates[curr_idx]

            if curr_sum > target:
                return

            if curr_sum == target and curr_path not in res:
                res.append(curr_path)

            for i in range(curr_idx + 1, len(candidates)):
                helper(i, curr_path[:], curr_sum)

        candidates.sort()
        for i in range(len(candidates)):
            helper(i, [], 0)

        return res


testCases = [
    ([2,3,6,7], 7),  # [[7]]
    ([2,3,5], 8),    # [[3,5]]
    ([10,1,2,7,6,1,5], 8),    # [[3,5]] 1 1 2 5 6 7 10
]

s = Solution()
for t in testCases:
    print(s.combinationSum2(t[0], t[1]))