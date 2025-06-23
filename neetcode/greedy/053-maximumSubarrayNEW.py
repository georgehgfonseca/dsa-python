from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = max(nums[0], 0)
        for i in range(1, len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)
        return maxSum


testCases = [
    [-2, 1],  # 1
    [-2, -1],  # -1
    [3, 2, -3, -1, 1, -3, 1, -1],  # 5
    # [-1,-2],    # -1
    # [0,-3,1,1], # 2
    # [-2,-3,-1],
    [5, 4, -1, 7, 8],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    # [1],
]

s = Solution()
for t in testCases:
    print(s.maxSubArray(t))

    # sum_left = [0]
    # for i in range(1, len(nums)):
    #     sum_left.append(sum_left[-1] + nums[i - 1])

    # sum_right = [0]
    # for i in range(len(nums) - 2, -1, -1):
    #     sum_right.insert(0, nums[i+1] + sum_right[0])

    # idx_min_sum_left = 0
    # min_sum_left = float("inf")
    # for i in range(len(sum_left)):
    #     if min_sum_left > sum_left[i]:
    #         idx_min_sum_left = i
    #         min_sum_left = sum_left[i]

    # idx_min_sum_right = 0
    # min_sum_right = float("inf")
    # for i in range(idx_min_sum_left, len(sum_right)):
    #     if min_sum_right > sum_right[i]:
    #         idx_min_sum_right = i
    #         min_sum_right = sum_right[i]

    # if idx_min_sum_left == idx_min_sum_right:
    #     return max(nums)

    # return sum(nums[idx_min_sum_left : idx_min_sum_right + 1])
    # if idx_min_sum_left <= idx_min_sum_right:
    #     return sum(nums[idx_min_sum_left : idx_min_sum_right + 1])
    # return max(nums)
