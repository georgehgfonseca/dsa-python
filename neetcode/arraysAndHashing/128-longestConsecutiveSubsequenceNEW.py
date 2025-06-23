from typing import List

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)

        res = 1
        for num in nums:
            if num + 1 in num_set and num - 1 not in num_set:
                # num is the beggining of a sequence
                seq_length = 2
                next = num + 2
                while next in num_set:
                    seq_length += 1
                    next += 1
                res = max(seq_length, res)
        return res








test_cases = [[100,4,200,1,3,2], 
              [0,3,7,2,5,8,4,6,0,1]]
s = Solution()
for t in test_cases:
    print(s.longestConsecutive(t))

