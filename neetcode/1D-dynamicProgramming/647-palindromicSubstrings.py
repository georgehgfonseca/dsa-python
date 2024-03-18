from typing import List
from collections import deque

class Solution:
    def countSubstrings(self, s: str) -> int:
        # wrong answer

        # count all substrings, including iif is palindrome
        palindrome_substr_count = {(s[i], i): 1 for i in range(len(s))} # (letter, index)
        substrs_to_check = deque((s[i], i) for i in range(len(s))) # (substr, starting_idx)

        def is_palindrome(s):
            for i in range((len(s) // 2) + 1):
                if s[i] != s[-(i + 1)]:
                    return False
            return True

        while substrs_to_check:
            (substr, i) = substrs_to_check.popleft()
            
            if i != 0:
                substr_plus_left = s[i - 1] + substr
                
                if is_palindrome(substr_plus_left):
                    palindrome_substr_count[(substr_plus_left, i - 1)] = palindrome_substr_count[(substr, i)] + 1
                    substrs_to_check.append((substr_plus_left, i - 1))
            
            index_next_char = i + len(substr)

            if index_next_char < len(s) - 1:
                substr_plus_right = substr + s[index_next_char] 

                if is_palindrome(substr_plus_right):
                    palindrome_substr_count[(substr_plus_right, i)] = palindrome_substr_count[(substr, i)] + 1
                    substrs_to_check.append((substr_plus_right, i))

        res = 0
        for substr in palindrome_substr_count:
            res += palindrome_substr_count[substr]

        return palindrome_substr_count

testCases = [
"abc", "aba", "aaa"
]

s = Solution()
for t in testCases:
    print(s.countSubstrings(t))