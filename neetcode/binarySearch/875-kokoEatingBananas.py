from typing import List
import math

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h == len(piles):
            return max(piles)

        lower_bound = math.ceil(sum(piles) / h)
        upper_bound = max(piles)

        # try each k >= lower_bound value of return the first
        eating_speed = lower_bound
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            eating_speed = mid
            min_hours = 0
            for i in range(len(piles)):
                min_hours += math.ceil(piles[i] / eating_speed)
            if min_hours <= h:
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1
                
        # double check eating_speed (test-case failed)
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i] / eating_speed)
        if hours <= h:
            return eating_speed
        else:
            return eating_speed + 1

        # TLE
        # if h == len(piles):
        #     return max(piles)

        # lower_bound = math.ceil(sum(piles) / h)

        # # try each k >= lower_bound value of return the first
        # eating_speed = lower_bound
        # while True:
        #     min_hours = 0
        #     for i in range(len(piles)):
        #         min_hours += math.ceil(piles[i] / eating_speed)
        #     if min_hours <= h:
        #         return eating_speed

        #     eating_speed += 1        

testCases = [
    ([1000000000,1000000000], 3), # 312884470
    ([7], 6), # 312884470
    ([312884470], 312884469), # 312884470
    ([3,6,7,11], 8),          # 4
    ([30,11,23,4,20], 5),     # 30
    ([30,11,23,4,20], 6),     # 23
]

s = Solution()
for t in testCases:
    print(s.minEatingSpeed(t[0], t[1]))