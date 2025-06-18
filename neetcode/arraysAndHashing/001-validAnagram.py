from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_count = dict()
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        for letter in t:
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            else:
                letter_count[letter] -= 1
        return True

test_cases = [("racecar", "carrace"), ("jar", "jam")]
s = Solution()
for t in test_cases:
    print(s.isAnagram(t[0], t[1]))

