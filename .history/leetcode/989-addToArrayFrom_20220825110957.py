from typing import List

# assuming it is forbidden to just convert into integers
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = num[:]
        kArr = []
        while k > 0:
            digit = k % 10
            k = k // 10
            kArr = [digit] + kArr
        buffer = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] + buffer > 9:
                ans[i] = 0
                buffer = 1
            else:
                ans[i] += 1
                return ans
        if buffer == 1:
            ans = [1] + ans
        return ans


testCases = [([1, 2, 0, 0], 34)]
s = Solution()
for t in testCases:
    print(s.addToArrayForm(t[0], t[1]))
