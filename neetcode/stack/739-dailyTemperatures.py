from typing import List
import math

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # had to look at the intuition in the video

        # index of the temperatures that did not yet found a warmer one
        index_stack_temps = list([0])
        ans = [0 for _ in temperatures]
        for i in range(1, len(temperatures)):
            if index_stack_temps and temperatures[i] > temperatures[index_stack_temps[-1]]:
                # pop all temperatures that found a higher one
                j = len(index_stack_temps) - 1
                while j >= 0:
                    index_top_of_stack = index_stack_temps[j]
                    if temperatures[i] > temperatures[index_top_of_stack]:
                        ans[index_top_of_stack] = i - index_top_of_stack
                        index_stack_temps.pop()
                        j -= 1
                    else:
                        break

            index_stack_temps.append(i)

        return ans

 
        # Brute force solution O(n^2)
        # ans = [0 for _ in temperatures]
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j - i
        #             break
        # return ans

                     
testCases = [
    [73,74,75,71,69,72,76,73],  # [1,1,4,2,1,1,0,0]
    # 0  1  2  3  4  5  6  7
    # i:     1
    # stack: [0]
    # temp:  []
    # ans:   []
    [5,6,2,1,7,6,3],            # [1,3,2,1,0,0,0]
    #0 1 2 3 4 5 6
    # i    : 6
    # stack: [4,5,6]
    # ans  : [1,3,2,1,0,0,0]
    # temp:  []
    [30,40,50,60],              # [1,1,1,0]
] 

s = Solution()
for t in testCases:
    print(s.dailyTemperatures(t))
