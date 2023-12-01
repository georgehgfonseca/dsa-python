from typing import List

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        # had to look the idea at the video solution

        start = 0
        end = 0
        max_len = 0
        # tracks, for each char, how many occurencies in window betwen start and end
        char_usage = {}

        while end < len(s):
            curr_char = s[end]
            if curr_char not in char_usage:
                char_usage[curr_char] = 1
            else:
                char_usage[curr_char] += 1

            occurencies_most_used_char = 0
            for char in char_usage:
                occurencies_most_used_char = max(char_usage[char], occurencies_most_used_char)
            
            is_valid_substr = (end + 1 - start) - occurencies_most_used_char <= k

            if is_valid_substr:
                max_len = max(max_len, (end + 1 - start))
            else:
                char_usage[s[start]] -= 1
                start += 1

            end += 1

        return max_len


testCases = [
    ("ABAB", 2),    # 2
    # start: 0
    # end:   0
    ("AABABBA", 1)  # 1
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