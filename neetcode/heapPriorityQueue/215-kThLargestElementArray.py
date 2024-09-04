from typing import List
import heapq

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_nums = [-num for num in nums]
        heapq.heapify(heap_nums)

        nth_largest = None
        for _ in range(k):
            nth_largest = heapq.heappop(heap_nums)

        return -nth_largest

    def findKthLargestSorting(self, nums: List[int], k: int) -> int:
        # could use heapq but time complexity would still be O(n log n)
        # with sorting O(n log n)
        nums.sort()
        return nums[-k]

testCases = [
    ([3,2,1,5,6,4], 2),         # 5
]

s = Solution()
for t in testCases:
    print(s.findKthLargest(t[0], t[1]))