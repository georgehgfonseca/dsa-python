from typing import List

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0: 
            return len(s)
        l, r = 0, 1
        char_set = {s[l]: l}
        maxLength = 1
        while r < len(s):
            if s[r] not in char_set:
                char_set[s[r]] = r
            else:
                l = char_set[s[r]] + 1
                r = l
                char_set = {s[l]: l}
            maxLength = max(maxLength, len(char_set))
            r += 1
        return maxLength

testCases = [
    "abcabcbb",    # 3
    "abcacbcbb",   # 3
    "aab",         # 2
    "dvdf",        # 3
    "bbbbb"        # 1
    ] 

s = Solution()
for t in testCases:
    print(s.lengthOfLongestSubstring(t))