from typing import List


class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        ans = []
        nextIdx = 0
        Q = [cand[nextIdx]]
        QSum = cand[nextIdx]
        while Q:
            if combSum + Q[-1] < target:
                combSum += Q[-1]
                Q.append(Q[-1])
                QSum += cand[Q[-1]]
            else:
                if combSum + Q[-1] == target:
                    ans.append(Q + [Q[-1]])
                QSum -= cand[Q[-1]]
                Q.pop()
                nextIdx += 1
                Q.append(cand[nextIdx])
                QSum += cand[nextIdx]
        return ans


testCases = [([2, 3, 5], 8)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
