from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        while first < last:
            diff = numbers[first] + numbers[last] - target
            if diff == 0:
                return [first+1, last+1]
            elif diff > 0:
                last -= 1
            else:
                first += 1
        

test_cases = [
    ([2,7,11,15], 9),
    # 2 + 15 - 9 = 8
    ([2,3,4], 6)]
s = Solution()
for t in test_cases:
    print(s.twoSum(t[0], t[1]))

