from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_splitted = []
        s_row = []
        i = 0
        row = 0
        while i < len(s):
            s_row.append(s[i])
            if (i + 1) % numRows == 0:
                s_splitted.append(s_row)
                s_row = []
                row += 1
            i += 1
        # TODO not solved

        


testCases = [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4)]
s = Solution()
for t in testCases:
    print(s.convert(t[0], t[1]))
