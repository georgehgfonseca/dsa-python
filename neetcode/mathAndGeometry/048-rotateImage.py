from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # copied from neetcode
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1

        # for i in range(len(matrix) - 1):
        #     for j in range(len(matrix) - 1):
        #         # rotate square
        #         newI = j
        #         newJ = len(matrix) - 1 - i
        #         while newI != i and newJ != j:
        #             temp = matrix[newI][newJ]
        #             matrix[newI][newJ] = matrix[i][j]
        #             newI = j
        #             newJ = len(matrix) - 1 - i

        #         newI = j
        #         newJ = len(matrix) - 1 - i
        #         temp = matrix[newI][newJ]
        #         matrix[newI][newJ] = matrix[i][j]
        #         matrix[i][j] = temp

        # new = [[None for _ in range(len(matrix))] for _ in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         newI = j
        #         newJ = len(matrix) - 1 - i
        #         new[newI][newJ] = matrix[i][j]
        # return new
        
testCases = [
    [[1,2,3],  # [7,4,1]
     [4,5,6],  # [8,5,2]
     [7,8,9]]  # [9,6,3]
]

s = Solution()
for t in testCases:
    s.rotate(t)
    print(t)





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
    
