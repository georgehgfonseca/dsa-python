from typing import List

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        # had to look the idea at the video solution
        # fails for test case 2
        char_count = {}
        l = r = 0
        res = 0
        maxFrequency = 0
        while r < len(s):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            maxFrequency = max(maxFrequency, char_count[s[r]])
            if r - l + 1 - maxFrequency <= k:
                res = max(res, r - l + 1)
                r += 1

            while (r - l + 1) - maxFrequency > k:
                char_count[s[l]] -= 1
                l += 1
        return res



testCases = [
    ("ABAB", 2),    # 4
    # start: 0
    # end:   0
    ("AABABBA", 1)  # 4
    # 0123456
    # start:      0
    # end:        4
    # char_usage: {A:3,B:2}
    # occurenes:  3
    # max_len:    4
]

s = Solution()
for t in testCases:
    print(s.characterReplacement(t[0], t[1]))