from typing import List


class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        ans = []
        nextIdx = 0
        Q = [cand[nextIdx]]
        QSum = cand[nextIdx]
        while Q:
            if QSum + Q[cand[nextIdx]] < target:
                QSum += Q[cand[nextIdx]]
                Q.append(Q[cand[nextIdx]])
            else:
                if QSum + Q[cand[nextIdx]] == target:
                    ans.append(Q + [Q[cand[nextIdx]]])
                QSum -= Q[cand[nextIdx]]
                Q.pop()
                nextIdx += 1
                if nextIdx >= len(cand):
                    nextIdx = cand.index(Q[-1]) + 1
                    QSum -= Q[-1]
                    Q.pop()
                # QSum += cand[nextIdx]
                # Q.append(cand[nextIdx])
        return ans


testCases = [([2, 3, 5], 8)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
