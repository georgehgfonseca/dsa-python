from typing import List

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_set = set()
        start = 0
        len_largests_char_set = 0
        for end in range(len(s)):
            while s[end] in chars_set:
                chars_set.remove(s[start])
                start += 1
            
            chars_set.add(s[end])
            len_largests_char_set = max(len_largests_char_set, len(chars_set))
        return len_largests_char_set
            






testCases = [
    "abcabcbb",    # 3
    # "abcacbcbb",   # 3
    # "bbbbb"
    ]       # 1

s = Solution()
for t in testCases:
    print(s.lengthOfLongestSubstring(t))