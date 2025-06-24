from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []

        def helper(root):
            if not root:
                return

            helper(root.left)
            helper(root.right)
            ans.append(root.val)
        
        helper(root)
        return ans

tree0 = TreeNode(3, 
                 TreeNode(1,
                          TreeNode(0),
                          TreeNode(2)), 
                 TreeNode(5, 
                          TreeNode(4),
                          TreeNode(6)))
tree1 = TreeNode(2, 
                 TreeNode(1), 
                 TreeNode(3))
tree2 = TreeNode(2, 
                 TreeNode(2), 
                 TreeNode(2))
tree3 = TreeNode(5, 
                 TreeNode(1), 
                 TreeNode(4, 
                          TreeNode(3), 
                          TreeNode(6)))

testCases = [
    tree0, 
    tree1, 
    tree2, 
    tree3, 
]

s = Solution()
for t in testCases:
    print(s.postorderTraversal(t))