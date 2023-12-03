from typing import List
import math

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # stack_idx_days_without_warmer = list()
        # for i in range(1, len(temperatures)):



        # start = 0
        # end = 1
        # ans = [0 for _ in temperatures]
        # while end < len(temperatures):
        #     if temperatures[start] < temperatures[end]:
        #         # found a warmer day for start
        #         ans[start] = end - start
        #         start += 1
        #     end += 1

        # Brute force solution O(n^2)
        ans = [0 for _ in temperatures]
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans


        # stack_temps_without_warmer_day = list()
        # days_without_warmer_day = [0 for _ in temperatures]

                 
        
    
testCases = [
    [73,74,75,71,69,72,76,73],  # [1,1,4,2,1,1,0,0]
    [30,40,50,60],              # [1,1,1,0]
] 

s = Solution()
for t in testCases:
    print(s.dailyTemperatures(t))
