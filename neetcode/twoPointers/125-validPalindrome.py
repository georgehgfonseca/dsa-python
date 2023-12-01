from typing import List

class Solution:

    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for letter in s:
            if self.alphanum(letter):
                clean_s += letter.lower()

        i = 0
        while i < len(clean_s) // 2:
            if clean_s[i] != clean_s[len(clean_s) - 1 - i]:
                return False
            i += 1
        return True

    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
    

test_cases = ["A man, a plan, a canal: Panama",
              "race a car",
              "abba",
              "ababa",
              " "]
s = Solution()
for t in test_cases:
    print(s.isPalindrome(t))

