from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Convert Tree to arr
        def helper(root):
            if root:
                if root.left and root.right:
                    return helper(root.left) + [root.val] + helper(root.right)
                if root.left and not root.right:
                    return helper(root.left) + [root.val]
                if not root.left and root.right:
                    return [root.val] + helper(root.right)
                if not root.left and not root.right:
                    return [root.val]
            else:
                return []
            
        return helper(root)[k - 1]

        

t1 = (TreeNode(3, 
              TreeNode(1,
                       None,
                       TreeNode(2)), 
              TreeNode(4)), 
    1)
t2 = (TreeNode(5, 
              TreeNode(3,
                       TreeNode(2, 
                                TreeNode(1), 
                                None),
                       TreeNode(4)), 
              TreeNode(6,
                       None,
                       TreeNode(7, 
                                None,
                                None))),
    3)

testCases = [t1, t2]
s = Solution()
for t in testCases:
    print(s.kthSmallest(t[0], t[1]))
