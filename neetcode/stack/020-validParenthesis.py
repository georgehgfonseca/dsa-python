from typing import List

class Solution:

    def isValid(self, s: str) -> bool:
        stack = list()
        map_paranthesis = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char not in map_paranthesis:
                # is an opening parenthesis
                stack.append(char)
            else:
                # is a closing parenthesis
                if stack and stack[-1] == map_paranthesis[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    
testCases = [
    "(){}}{",   # False 
    "()",       # True 
    "(]",       # False
    "()[]{}"]   # True

s = Solution()
for t in testCases:
    print(s.isValid(t))