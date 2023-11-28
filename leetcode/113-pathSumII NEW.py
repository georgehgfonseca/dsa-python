from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def helper(root, curr_path, curr_sum, ans, targetSum):
            if root:
                curr_path += [root.val]
                curr_sum += root.val
                if curr_sum == targetSum and not root.left and not root.right:
                        ans.append(curr_path)
                helper(root.left, curr_path[:], curr_sum, ans, targetSum)
                helper(root.right, curr_path[:], curr_sum, ans, targetSum)

        if not root:
            return []
        
        ans = []
        helper(root, [], 0, ans, targetSum)
        return ans



t = TreeNode(1, 
             TreeNode(2, 
                      None, 
                      TreeNode(5)), 
             TreeNode(3))
t2 = TreeNode(1, 
              TreeNode(2, 
                       TreeNode(4), 
                       TreeNode(5)), 
              TreeNode(3, 
                       TreeNode(6), 
                       TreeNode(7)))
t3 = TreeNode(1, 
              TreeNode(2), 
              None)
# [1,-2,-3,1,3,-2,null,-1]
t4 = TreeNode(1, 
              TreeNode(-2, 
                       TreeNode(1, 
                                TreeNode(-1), 
                                None), 
                       TreeNode(3)), 
              TreeNode(-3, 
                       TreeNode(-2), 
                       None))

testCases = [(t, 8), (t2, 10), (t3, 1), (t4, -1)]
s = Solution()
for t in testCases:
    print(s.pathSum(t[0], t[1]))
