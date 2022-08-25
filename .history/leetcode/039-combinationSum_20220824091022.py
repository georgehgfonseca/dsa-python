from typing import List


class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        cand.sort()
        ans = []
        nextIdx = 0
        Q = [cand[nextIdx]]
        QSum = cand[nextIdx]
        while Q:
            if QSum == target:
                ans.append(Q[:])
            if QSum + Q[-1] < target:
                QSum += Q[-1]
                Q.append(Q[-1])
            else:
                if QSum + Q[-1] == target:
                    ans.append(Q[:] + [Q[-1]])
                QSum -= Q[-1]
                Q.pop()
                nextIdx += 1
                if nextIdx >= len(cand):
                    if not Q:
                        return ans
                    nextIdx = cand.index(Q[-1]) + 1
                    if nextIdx >= len(cand):
                        return ans
                    QSum -= Q[-1]
                    Q.pop()
                QSum += cand[nextIdx]
                Q.append(cand[nextIdx])
        return ans


testCases = [([7, 3], 17), ([2, 7, 6, 3, 5, 1], 9), ([1], 1), ([2, 3, 5], 8), ([2, 3, 6, 7], 7)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
