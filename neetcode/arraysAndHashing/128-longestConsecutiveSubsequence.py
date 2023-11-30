from typing import List

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_seq_len = 0
        for num in nums:
            seq_len = 0
            if num - 1 not in num_set:
                seq_len += 1
                next_num = num + 1
                while next_num in num_set:
                    seq_len += 1
                    next_num += 1
                if seq_len > max_seq_len:
                    max_seq_len = seq_len
        return max_seq_len



test_cases = [[100,4,200,1,3,2], 
              [0,3,7,2,5,8,4,6,0,1]]
s = Solution()
for t in test_cases:
    print(s.longestConsecutive(t))

