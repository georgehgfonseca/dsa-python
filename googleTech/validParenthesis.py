from typing import List
from collections import deque

class Solution:

    def isValid(self, s: str) -> bool:
        openning_chars = {"(", "{", "["}
        closing_chars = {")", "}", "]"}
        opposit_map = {")": "(", "}": "{", "]": "["}

        open_chars = deque()
        for letter in s:
            if letter in openning_chars:
                open_chars.append(letter)
            else:
                if not open_chars:
                    return False

                last_open_char = open_chars.pop()
                if last_open_char != opposit_map[letter]:
                    return False
        
        return True

    
testCases = [
    "(){}}{",   # False 
    "()",       # True 
    "(]",       # False
    "()[]{}"]   # True

s = Solution()
for t in testCases:
    print(s.isValid(t))