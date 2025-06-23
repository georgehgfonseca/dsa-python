from typing import List
import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap to count occurencies
        numCount = dict()
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1

        # O(n log n)
        numCountSorted = sorted(
            numCount.items(), key=lambda item: item[1], reverse=True
        )
        ans = []
        for i in range(k):
            ans.append(numCountSorted[i][0])
        return ans

        # O(n * k)
        # then iterate k times over the hashmap's keys to get the k-th most frequente element
        # [3, 0, 1, 0]
        # {3: 1, 0: 2, 1: 1}
        ans = []
        for _ in range(k):
            currMax = None
            maxCount = 0
            for num in numCount:
                if numCount[num] > maxCount:
                    currMax = num
                    maxCount = numCount[num]
            if currMax == None:
                raise Exception("Could not count the k-th most frequent element")
            ans.append(currMax)
            numCount.pop(currMax)
        return ans


test_cases = [
    ([4, 1, -1, 2, -1, 2, 3], 2),  # [2, -1]
    ([3, 0, 1, 0], 1),  # [0]
    ([1, 1, 1, 2, 2, 3], 2),  # [1, 2]
    ([1], 1),  # [1]
    ([1, 5, 5, 3, 3], 2),
]  # [3, 5]
s = Solution()
for t in test_cases:
    print(s.topKFrequent(t[0], t[1]))
