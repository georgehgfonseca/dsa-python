class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # enumeration - decision: add or not a dot on the index
        # base case: all 3 dots were added or index out of bounds
        def validChunk(chunk):
            if chunk[0] == "0" and len(chunk) > 1:
                return False
            return 0 <= int(chunk) <= 255

        res = []
        def dfs(idx, remainingDots, curr):
            chunk = curr.split(".")[-1]
            if not validChunk(chunk):
                return
            if idx >= len(s):
                if remainingDots == 0:
                    res.append(curr)
                return

            if remainingDots > 0:
                dfs(idx + 1, remainingDots - 1, curr + "." + s[idx])
            dfs(idx + 1, remainingDots, curr + s[idx])
        
        dfs(1, 3, s[0])
        return res
            

        # dfs(idx, remainingDots, curr)
        # 101023
        # dfs(1, 3, "1")
        # -- ADD dfs(2, 2, "1.0")
        # ---- ADD dfs(3, 2, "1.0.1")
        # ------ ADD dfs(4, 1, "1.0.1.0") # return
        # ------ NOT dfs(4, 1, "1.0.10")
        # -------- ADD dfs(5, 0, "1.0.10.2")
        # ---------- NOT dfs(6, 0, "1.0.10.23")
        # -------- NOT dfs(4, 1, "1.0.102")
        # ---------- ADD dfs(4, 0, "1.0.102.3") # add 1.0.102.3
        # ---------- NOT dfs(4, 1, "1.0.1023") # return
        # ---- NOT dfs(3, 3, "101")
        # ------ ADD dfs(4, 2, "101.0")
        # -------- ADD dfs(5, 1, "101.0.2")
        # ---------- ADD dfs(6, 0, "101.0.2.3") # add 101.0.2.3
        # ---------- NOT dfs(6, 1, "101.0.23") # return
        # -------- NOT dfs(5, 2, "101.02") # return
        # ------ NOT dfs(4, 3, "1010") # return
        # -- NOT dfs(2, 3, "10")
