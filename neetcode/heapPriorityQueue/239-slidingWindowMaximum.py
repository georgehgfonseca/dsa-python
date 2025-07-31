import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # n log(k)
        window = [(-nums[i], i) for i in range(k)]
        heapq.heapify(window)
        res = [window[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(window, (-nums[i], i))
            idxSmallestElem = window[0][1]
            smallestIdxWindow = i - k + 1

            while smallestIdxWindow > idxSmallestElem:
                heapq.heappop(window)
                idxSmallestElem = window[0][1]

            res.append(window[0][0])
        
        return [-val for val in res]
        