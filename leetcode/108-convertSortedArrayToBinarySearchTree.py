from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if nums == []:
            return None
        
        mid = (len(nums) - 1) // 2
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[0:mid]), self.sortedArrayToBST(nums[mid + 1:]))


testCases = [[-10,-3,0,5,9], [1,3]]
s = Solution()
for t in testCases:
    print(s.sortedArrayToBST(t))
