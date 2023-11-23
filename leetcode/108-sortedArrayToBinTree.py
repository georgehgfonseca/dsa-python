from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, arr: List[int]) -> Optional[TreeNode]:
        if arr:
            return TreeNode(
                arr[len(arr) // 2],
                self.sortedArrayToBST(arr[: len(arr) // 2]),
                self.sortedArrayToBST(arr[(len(arr) // 2) + 1 :]),
            )

        # def insertNode(arr):
        #     if arr:
        #         return TreeNode(
        #             arr[len(arr) // 2],
        #             insertNode(arr[: len(arr) // 2]),
        #             insertNode(arr[(len(arr) // 2) + 1 :]),
        #         )

        # return insertNode(arr)


testCases = [[-10, -3, 0, 5, 9]]
s = Solution()
for t in testCases:
    print(s.sortedArrayToBST(t))

    # def binSearch(arr, target):
    #     low = 0
    #     high = len(arr) - 1
    #     while low <= high:
    #         mid = high + low // 2
    #         if arr[mid] == target:
    #             return mid
    #         elif arr[mid] > target:
    #             high = mid - 1
    #         else:
    #             low = mid + 1
    #     return -1 # not found
