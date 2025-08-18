# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # TODO: had to watch the video and code implementation
        
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None

            inorderIdx = {inorder[i]: i for i in range(len(inorder))}
            root = TreeNode(preorder[0])
            mid = inorderIdx[preorder[0]]

            root.left = dfs(preorder[1:mid + 1], inorder[:mid])
            root.right = dfs(preorder[mid + 1:], inorder[mid + 1:])
            return root
        
        return dfs(preorder, inorder)
