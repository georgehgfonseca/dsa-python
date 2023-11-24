from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # def helper(root1, root2):
        #     if root1 and root2:
        #         return TreeNode(root1.val + root2.val, helper(root1.left, root2.left), helper(root1.right, root2.right))
        #     if root1 and not root2:
        #         return root1
        #     if root2 and not root1:
        #         return root2
            
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1  

        # return helper(root1, root2)

        def helper(root1, root2):
            # Update val for root1 node
            if root1 and root2:
                root1.val = root1.val + root2.val
            if root2 and not root1:
                root1 = root2
                return 
            
            # Move to children
            if root1.left and root2.left:
                helper(root1.left, root2.left)
            if root1.right and root2.right:
                helper(root1.right, root2.right)
            if root2.left and not root1.left:
                root1.left = root2.left
            if root2.right and not root1.right:
                root1.right = root2.right

        if not root1:
            return root2
        if not root2:
            return root1            

        helper(root1, root2)
        return root1

t1 = TreeNode(1, 
              TreeNode(3,
                       TreeNode(5, 
                                None, 
                                None),
                       None), 
              TreeNode(2,
                       None,
                       None))
t2 = TreeNode(2, 
              TreeNode(1,
                       None,
                       TreeNode(4, None,
                                None)), 
              TreeNode(3,
                       None,
                       TreeNode(7, 
                                None,
                                None)))

testCases = [(t1, t2)]
s = Solution()
for t in testCases:
    print(s.mergeTrees(t[0], t[1]))
