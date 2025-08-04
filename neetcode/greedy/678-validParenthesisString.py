class Solution:
    def checkValidStringGreedy(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
        
    def checkValidString(self, s: str) -> bool:
        dp = dict()

        def dfs(i, open):
            if (i, open) in dp:
                return dp[(i, open)]
            if open < 0:
                return False
            if i >= len(s):
                return open == 0

            if s[i] == "(":
                res = dfs(i + 1, open + 1)
            elif s[i] == ")":
                res = dfs(i + 1, open - 1)
            else:
                # adds a "(", ")", or " "
                res = dfs(i + 1, open + 1) or dfs(i + 1, open - 1) or dfs(i + 1, open)

            dp[(i, open)] = res
            return res
            
        return dfs(0, 0)
    
    def checkValidString2(self, s: str) -> bool:

        def dfs(i, open):
            if open < 0:
                return False
            if i >= len(s):
                return open == 0

            if s[i] == "(":
                return dfs(i + 1, open + 1)
            elif s[i] == ")":
                return dfs(i + 1, open - 1)
            else:
                # adds a "(", ")", or " "
                return dfs(i + 1, open + 1) or dfs(i + 1, open - 1) or dfs(i + 1, open)
        
        return dfs(0, 0)