from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(nums):
            if not nums:
                return None
            mid = (len(nums) - 1) // 2
            return TreeNode(nums[mid], helper(nums[:mid]), helper(nums[mid + 1:]))
        
        return helper(nums)




testCases = [[-10,-3,0,5,9], [1,3]]
s = Solution()
for t in testCases:
    print(s.sortedArrayToBST(t))
