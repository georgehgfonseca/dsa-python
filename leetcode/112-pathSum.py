from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, currSum, targetSum):
            currSum += root.val
            if not root.left and not root.right:
                if currSum == targetSum:
                    return True
                else:
                    return False
            if root.left and root.right:
                return helper(root.left, currSum, targetSum) or helper(root.right, currSum, targetSum)
            if root.left:
                return helper(root.left, currSum, targetSum)
            if root.right:
                return helper(root.right, currSum, targetSum)

        if root:
            return helper(root, 0, targetSum)
        else:
            return False



t = (TreeNode(1, 
              TreeNode(2, 
                       None, 
                       None), 
              TreeNode(3, 
                       None, 
                       None)), 3)  # [1,2,3]
t2 = (TreeNode(5, 
               TreeNode(4, 
                        TreeNode(11, 
                                 TreeNode(7, 
                                          None, 
                                          None), 
                                 TreeNode(2, 
                                          None, 
                                          None)), 
                        None), 
               TreeNode(8, 
                        TreeNode(13, 
                                 None, 
                                 None), 
                        TreeNode(4, 
                                 None,
                                 TreeNode(1,
                                          None, 
                                          None)))), 22)  # [5,4,8,11,null,13,4,7,2,null,null,null,1]
t3 = (TreeNode(1, 
              TreeNode(2, 
                       None, 
                       None),
              None), 1)  # [1,2,null]
t4 = (TreeNode(-2, 
              None,
              TreeNode(-3, 
                       None, 
                       None)), -5)  # [-2,null,-3]

testCases = [t, t2, t3, t4]
s = Solution()
for t in testCases:
    print(s.hasPathSum(t[0], t[1]))
