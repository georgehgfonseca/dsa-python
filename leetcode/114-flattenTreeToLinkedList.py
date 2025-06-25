# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            if not root:
                return
            
            temp = root.right
            root.right = root.left
            root.left = None
            # move add temp to the rightmost postion of root.right
            curr = root
            while curr.right:
                curr = curr.right
            curr.right = temp

            dfs(root.right)

        dfs(root)
        return root