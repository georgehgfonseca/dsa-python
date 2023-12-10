from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(cur, numOpenParenthesis, numRemParenthesis):
            if not numRemParenthesis and numOpenParenthesis == 0:
                # found new combination
                res.append(cur)
                return
            if numRemParenthesis > 0:
                # create combination openning parenthesis
                helper(cur[:] + "(", numOpenParenthesis + 1, numRemParenthesis - 1)
            if numOpenParenthesis > 0:
                # create combination closing parenthesis
                helper(cur[:] + ")", numOpenParenthesis - 1, numRemParenthesis)
          
        helper("(", 1, n-1)
        return res
    
testCases = [
    3, 
    2, 
    4]

s = Solution()
for t in testCases:
    print(s.generateParenthesis(t))