from typing import List


class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        Q = [cand[0]]
        ans = []
        nextIdx = 0
        while Q:
            combSum = 0
            comb = []
            if combSum + Q[-1] < target:
                comb.append(Q[-1])
                combSum += Q[-1]
                Q.append(Q[-1])
            else:
                if combSum + Q[-1] == target:
                    ans.append(Q + [Q[-1]])
                Q.pop()
                nextIdx += 1
                Q.append(cand[nextIdx])
        return ans


testCases = [([2, 3, 5], 8)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
