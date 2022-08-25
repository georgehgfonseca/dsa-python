from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(idx: int, comb: List[int], cand: List[int], partialTarget: int):
            if idx >= len(cand):
                return
            if cand[idx] == partialTarget:  # found a match
                ans.append(comb + [cand[idx]])
                return
            if cand[idx] < partialTarget:
                helper(idx, comb + [cand[idx]], cand, partialTarget - cand[idx])
            helper(idx + 1, comb[:-1], cand, partialTarget + comb[-1])

        helper(0, [], candidates, target)
        return ans

    def combinationSumRec(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def fun(index, comb, cand, partialTarget):
            if index == len(cand):
                if partialTarget == 0:
                    res.append(comb.copy())
                return
            if cand[index] <= partialTarget:
                comb.append(cand[index])
                fun(index, comb, cand, partialTarget - cand[index])
                comb.pop()
            fun(index + 1, comb, cand, partialTarget)

        fun(0, [], candidates, target)
        return res

    def combinationSumWA(self, cand: List[int], target: int) -> List[List[int]]:
        # WA for [7, 3, 2], 18
        cand.sort()
        ans = []
        nextIdx = 0
        S = [cand[nextIdx]]
        QSum = cand[nextIdx]
        while S:
            if QSum == target:
                ans.append(S[:])
            if QSum + S[-1] < target:
                QSum += S[-1]
                S.append(S[-1])
            else:
                if QSum + S[-1] == target:
                    ans.append(S[:] + [S[-1]])
                QSum -= S[-1]
                S.pop()
                nextIdx += 1
                if nextIdx >= len(cand):
                    if not S:
                        return ans
                    nextIdx = cand.index(S[-1]) + 1
                    if nextIdx >= len(cand):
                        return ans
                    QSum -= S[-1]
                    S.pop()
                QSum += cand[nextIdx]
                S.append(cand[nextIdx])
        return ans


testCases = [([2, 3, 6, 7], 7), ([7, 3, 2], 18), ([7, 3], 17), ([2, 7, 6, 3, 5, 1], 9), ([1], 1), ([2, 3, 5], 8)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
