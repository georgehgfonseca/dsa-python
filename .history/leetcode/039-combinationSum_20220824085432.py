from typing import List


class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        ans = []
        nextIdx = 0
        Q = [cand[nextIdx]]
        QSum = cand[nextIdx]
        while Q:
            if QSum + Q[-1] < target:
                QSum += Q[-1]
                Q.append(Q[-1])
            else:
                if QSum + Q[-1] == target:
                    ans.append(Q + [Q[-1]])
                QSum -= Q[-1]
                Q.pop()
                nextIdx += 1
                if nextIdx >= len(cand):
                    nextIdx = cand.index(Q[-1]) + 1
                    QSum -= Q[-1]
                    Q.pop()
                QSum += cand[nextIdx]
                Q.append(cand[nextIdx])
                if QSum == target:
                    ans.append(Q[:])

        return ans


testCases = [([2, 3, 5], 8)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
