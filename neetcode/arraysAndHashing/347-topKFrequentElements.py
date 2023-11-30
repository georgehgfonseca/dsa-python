from typing import List
import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_freq = {}
        heap = []
        for num in nums:
            if num not in num_freq:
                num_freq[num] = 1
            else:
                num_freq[num] += 1

        for num in num_freq:
            heapq.heappush(heap, (-num_freq[num], num))
        
        ans = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            ans.append(num)

        return ans

        # # using bucket sort
        # num_freq = {}
        # heap = []
        # for num in nums:
        #     if num not in num_freq:
        #         num_freq[num] = 1
        #     else:
        #         num_freq[num] += 1

        # freq_num = [[] for _ in range(len(nums) + 1)]
        # for num in num_freq:
        #     freq_num[num_freq[num]].append(num)
        
        # ans = []
        # remaining = k
        # for i in range(len(nums), -1, -1):
        #     remaining -= len(freq_num[i])
        #     ans += freq_num[i]
        #     if remaining == 0:
        #         break
        # return ans


test_cases = [
    ([1,1,1,2,2,3], 2), # [1, 2]
    ([1], 1),           # [1]
    ([1,5,5,3,3], 2)]   # [3, 5]
s = Solution()
for t in test_cases:
    print(s.topKFrequent(t[0], t[1]))

