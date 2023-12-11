from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy O(n) solution
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0

        # O(n^2) with DP deadEndIndexes info, otherwise O(n^n) 
        # deadEndIndexes = set()

        # self.achievedGoal = False
        # def helper(i):
        #     if not deadEndIndexes or i not in deadEndIndexes:
        #         if i == len(nums) - 1:
        #             self.achievedGoal = True
        #         if i < len(nums) - 1:
        #             # expand the search (eval all jump possibilities 1...nums[i])
        #             # for j in range(nums[i], 0, -1):
        #             for j in range(1, nums[i] + 1):
        #                 if i+j > len(nums) - 1:
        #                     break
        #                 helper(i+j)
        #     deadEndIndexes.add(i)


        # helper(0)
        # return self.achievedGoal

testCases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
]

s = Solution()
for t in testCases:
    print(s.canJump(t))