from typing import List


class Solution:

    def longestPalindrome(self, s: str) -> str:
        # O(n^2) solution
        largestSubstr = s[0]

        for i in range(0, len(s) - 1):
            # check for odd palindromes
            offset = 1
            while i - offset >= 0 and i + offset <= len(s) - 1:
                if s[i - offset] != s[i + offset]:
                    break
                offset += 1
            offset -= 1
            if offset * 2 + 1 > len(largestSubstr):
                largestSubstr = s[i - offset : i + offset + 1]

            if i + 1 < len(s) and s[i + 1] == s[i]:
                # check for even palindromes
                offsetEven = 1
                while i - offsetEven >= 0 and i + 1 + offsetEven <= len(s) - 1:
                    if s[i - offsetEven] != s[i + 1 + offsetEven]:
                        break
                    offsetEven += 1
                offsetEven -= 1
                if offsetEven * 2 + 2 > len(largestSubstr):
                    largestSubstr = s[i - offsetEven : i + offsetEven + 2]

        return largestSubstr

        # O(n^3) brute-force approach
        # def isPalindrome(s):
        #     i = 0
        #     while i < len(s) // 2:
        #         if s[i] != s[-(i+1)]:
        #             return False
        #         i += 1
        #     return True

        # largest = 1
        # largestSubstr = s[0]
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         # check if word from i to j is a palindrome
        #         substr = s[i:j+1]
        #         if isPalindrome(substr):
        #             if largest < len(substr):
        #                 largest = len(substr)
        #                 largestSubstr = substr

        # return largestSubstr


testCases = [
    "eabcb",
    "ccc",
    "cbbd" "bb",
    "babad",
    #           01234
    # i:        1
    # offset:   1
    # largest:  bab
]

s = Solution()
for t in testCases:
    print(s.longestPalindrome(t))
