from typing import List


class Solution:

    def longestPalindrome(self, s: str) -> str:
        maxLenght = 1
        ansIdx = [0, 1]
        for i in range(len(s)):
            j = 1
            currLenght = 1
            # odd lenght
            while i - j >= 0 and i + j < len(s):
                if s[i - j] != s[i + j]:
                    break
                currLenght += 2
                if currLenght > maxLenght:
                    maxLenght = currLenght
                    ansIdx = [i - j, i + j + 1]
                j += 1
            # even lenght
            if i + 1 < len(s) and s[i] == s[i + 1]:
                currLenght = 2
                if currLenght > maxLenght:
                    maxLenght = currLenght
                    ansIdx = [i, i + 2]
                j = 1
                while i - j >= 0 and i + 1 + j < len(s):
                    if s[i - j] != s[i + 1 + j]:
                        break
                    currLenght += 2
                    if currLenght > maxLenght:
                        maxLenght = currLenght
                        ansIdx = [i - j, i + 1 + j + 1]
                    j += 1
        return s[ansIdx[0] : ansIdx[1]]


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
