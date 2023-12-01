from typing import List

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        letters_in_substring = set()
        longest_len = 0
        while end < len(s):
            if s[end] not in letters_in_substring:
                letters_in_substring.add(s[end])
                longest_len = max(longest_len, len(letters_in_substring))
            else:
                # move to the position of repeated letter
                while s[end] != s[start]:
                    letters_in_substring.remove(s[start])
                    start += 1
                    if start > len(s) - 1:
                        return longest_len
                start += 1
            end += 1

        return longest_len


testCases = [
    "abcabcbb",    # 3
    "abcacbcbb",   # 3
    #012345678
    # start:           6
    # end:             9
    # letters_in_subs: {c,b}
    # longest_len:     3
    "bbbbb"]      # 1

s = Solution()
for t in testCases:
    print(s.lengthOfLongestSubstring(t))