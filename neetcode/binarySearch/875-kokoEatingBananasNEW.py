from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # there are bounds for k: 1 <= k <= min(max(piles), h)
        # do binary search over k values
        # for each k, evaluate if can eat
        # if can: search left of k
        # otherwise, search right of k
        # evaluate: divide each element by k and round up. sum the array
        # return the last succesful k value
        # piles      = [1, 4, 3, 2]
        # h          = 9
        # l          = 1
        # r          = 1
        # k          = 1
        # eval       = [1, 4, 3, 2]
        # hours      = sum(eval) = 10

        def canEat(piles: List[int], eatRate: int, hours: int):
            eatHours = [math.ceil(pile / eatRate) for pile in piles]
            return sum(eatHours) <= hours

        l, r = 1, max(piles)
        lastSuccessfullK = None
        while l <= r:
            k = (r + l) // 2
            if canEat(piles, k, h):
                lastSuccessfullK = k
                # try with smaller k
                r = k - 1
            else:
                # try with larger k
                l = k + 1
        return lastSuccessfullK 

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