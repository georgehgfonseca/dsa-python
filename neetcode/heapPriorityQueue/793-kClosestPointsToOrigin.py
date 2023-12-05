from typing import List
import heapq

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # compute the distances to origin and create a tuple
        dist_heap = []
        for point in points:
            dist = ((point[0] ** 2) + (point[1] ** 2)) ** (1/2)
            heapq.heappush(dist_heap, (dist, point))
        
        ans = list()
        for _ in range(k):
            dist, point = heapq.heappop(dist_heap)
            ans.append(point)

        return ans

testCases = [
    ([[1,3],[-2,2]], 1),         # [[-2,2]]
    ([[3,3],[5,-1],[-2,4]], 2),  # [[3,3],[-2,4]]
]

s = Solution()
for t in testCases:
    print(s.kClosest(t[0], t[1]))