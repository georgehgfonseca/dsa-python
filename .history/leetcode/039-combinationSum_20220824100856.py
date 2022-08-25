from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(idx: int, comb: List[int], cand: List[int], partialTarget: int, ans: List[List[int]]):
            if idx >= len(cand):
                return
            if cand[idx] == partialTarget:  # found a match
                ans.append(comb + [cand[idx]])
                return
            if cand[idx] < partialTarget:
                helper(idx, comb + [cand[idx]], cand, partialTarget - cand[idx], ans)
            else:
                helper(idx + 1, comb.pop(), cand, partialTarget, ans)

        helper(0, [], candidates, target, ans)
        return ans

    def combinationSumRec(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def fun(index, l, a, ts):
            if index == len(a):
                if ts == 0:
                    res.append(l.copy())
                return
            if a[index] <= ts:
                l.append(a[index])
                fun(index, l, a, ts - a[index])
                l.pop()
            fun(index + 1, l, a, ts)

        fun(0, [], candidates, target)
        return res

    def combinationSumWA(self, cand: List[int], target: int) -> List[List[int]]:
        # WA for [7, 3, 2], 18
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


testCases = [([2, 3, 6, 7], 7), ([7, 3, 2], 18), ([7, 3], 17), ([2, 7, 6, 3, 5, 1], 9), ([1], 1), ([2, 3, 5], 8)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
