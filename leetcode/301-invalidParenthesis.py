from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        open = ""
        res = [""]
        for i in range(len(s)):
            if s[i] != "(" and s[i] != ")":
                for r in range(len(res)):
                    res[r] += s[i]
                continue
            if s[i] == "(":
                for r in range(len(res)):
                    res[r] += s[i]
                open += s[i]
            elif s[i] == ")":
                if len(open) == 0:
                    # at least one correction must be made
                    k = 0
                    k_max = len(res)
                    while k < k_max:
                        r = res[k] + ")"
                        k += 1
                        for j in range(len(r) - 1):
                            if r[j] == ")":
                                # create a new answer removing this ')'
                                rNew = r[:j] + r[j + 1 :]
                                if rNew not in res:
                                    res.append(rNew)
                elif open[-1] == "(":
                    # remove open paranthesis
                    open = open[:-1]
                    for r in range(len(res)):
                        res[r] += s[i]
        # remove excessive open parenthesis
        for r in range(len(res)):
            max_c = len(res[r])
            idx_to_remove = []
            open = ""
            for c in range(max_c - 1, -1, -1):
                if res[r][c] == ")":
                    open += ")"
                elif res[r][c] == "(":
                    if len(open) == 0:
                        idx_to_remove.append(c)
                    elif open[-1] == ")":
                        open = open[:-1]
            for idx in idx_to_remove:
                res[r] = res[r][:idx] + res[r][idx + 1 :]
        return res


r1 = "()())()"
r2 = "(a)())()"
r3 = ")("
r4 = "(((k()(("  # fails
testCases = [r4]
s = Solution()
for r in testCases:
    print(s.removeInvalidParentheses(r))
