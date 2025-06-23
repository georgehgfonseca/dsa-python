from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [2, 1, 2, 3, 4]
        # k    = 1
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k

        # brute force
        tmp = []
        for num in nums:
            if num == val:
                tmp.append(num)

        for i in range(len(nums)):
            nums[i] = tmp[i]

        return len(tmp)


test_cases = [([1, 1, 2, 3, 4], 1), ([3, 2, 4], 2), ([3, 3], 3)]
s = Solution()
for t in test_cases:
    print(s.removeElement(t[0], t[1]))
