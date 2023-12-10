from typing import List

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by starting time
        intervals.sort(key=lambda x:x[0])
        print(intervals)

        merged = []
        i = 0
        while i < len(intervals):
            start_i, end_i = intervals[i][0], intervals[i][1]
            mergedWithI = [start_i, end_i]
            for j in range(i+1, len(intervals)):
                # overlap?
                start_j, end_j = intervals[j][0], intervals[j][1]
                if mergedWithI[1] >= start_j:
                    i += 1
                    mergedWithI = [min(mergedWithI[0], start_j), max(mergedWithI[1], end_j)]
                else:
                    break
            merged.append(mergedWithI)
            i += 1

        return merged


testCases = [
    [[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]],
    # [[1,3],[2,6],[8,10],[15,18]], # [[1,6],[8,10],[15,18]]
    # [[1,4],[0,4]], # 
    # [[1,4],[2,3]], # 
    # [[1,4],[0,2],[3,5]],
]

s = Solution()
for t in testCases:
    print(s.merge(t))
