from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # Using DP
        if numRows == 1:
            return [[1]]
        dp = [[] for i in range(numRows)]
        dp[0] = [1]
        dp[1] = [1, 1]
        for i in range(2, numRows):
            new = [1]
            for j in range(1, len(dp[i - 1])):
                new.append(dp[i - 1][j - 1] + dp[i - 1][j])
            new.append(1)
            dp[i] = new
        return dp
    
        # Using recursion
        # def helper(curr_row, curr_idx, ans):
        #     if curr_idx > numRows - 1:
        #         return

        #     temp = []
        #     for j in range(len(curr_row) - 1):
        #         temp.append(curr_row[j] + curr_row[j + 1])
            
        #     ans.append([1] + temp + [1])

        #     helper([1] + temp[:] + [1], curr_idx + 1, ans)
        
        # if numRows == 1:
        #     return [[1]]
        # elif numRows == 2:
        #     return [[1], [1, 1]]

        # ans = [[1], [1, 1]]
        # helper([1, 1], 2, ans)
        # return ans


testCases = [5, 1]
s = Solution()
for t in testCases:
    print(s.generate(t))
