class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        # fix dimensions
        length = max(len(a), len(b))
        if len(a) != length:
            a = "0" * (length - len(a)) + a
        if len(b) != length:
            b = "0" * (length - len(b)) + b
        buffer = 0
        for i in range(len(a) - 1, -1, -1):
            if a[i] == "1" and b[i] == "1":
                if buffer == 0:
                    ans = "0" + ans
                    buffer = 1
                else:
                    ans = "1" + ans
                    buffer = 1
            elif a[i] == "0" and b[i] == "0":
                if buffer == 0:
                    ans = "0" + ans
                    buffer = 0
                else:
                    ans = "1" + ans
                    buffer = 0
            else:  # either a[i] or b[i] is 1
                if buffer == 0:
                    ans = "1" + ans
                    buffer = 0
                else:
                    ans = "0" + ans
                    buffer = 1
        if buffer == 1:
            ans = "1" + ans
        return ans


testCases = [("11", "1"), ("1010", "1011")]
s = Solution()
for t in testCases:
    print(s.addBinary(t[0], t[1]))
