from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # intervals           = [[1,3],[2,3],[3,7],[6,6]]
        # queries             = [2,3,1,7,6,8]
        # k                   = 8
        # minLen              = inf
        # ans                 = [2, 2, 3, 5, 1]

        # sort intervals and queries
        intervals.sort()
        queryMinLen = {k: -1 for k in queries}
        queryMinLen = dict(sorted(queryMinLen.items()))
        checked = [False for _ in intervals]
        # for each query k, iterate over intervals
        for k in queryMinLen:
            minLen = float("inf")
            for i, (start, end) in enumerate(intervals):
                if checked[i]:
                    continue
                if k > end:
                    checked[i] = True
                if start <= k <= end:
                    minLen = min(minLen, end - start + 1)
                if start > k:
                    break
            if minLen != float("inf"):
                queryMinLen[k] = minLen
        # process original queries
        return [queryMinLen[k] for k in queries]

    def minIntervalBF(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        # brute force
        # sort intervals
        intervals.sort()
        # for each query k, iterate over intervals
        ans = []
        for k in queries:
            minLen = float("inf")
            for start, end in intervals:
                if start <= k <= end:
                    minLen = min(minLen, end - start + 1)
                if k < start:
                    break
            minLen = minLen if minLen != float("inf") else -1
            ans.append(minLen)
        return ans


testCases = [
    ([[1, 3], [2, 3], [3, 7], [6, 6]], [2, 3, 1, 7, 6, 8]),  # [2,2,3,5,1,-1]
    ([[4, 5], [5, 8], [1, 9], [8, 10], [1, 6]], [7, 9, 3, 9, 3]),  # [4,3,6,3,6]
]

s = Solution()
for t in testCases:
    print(s.minIntervalBF(t[0], t[1]))
