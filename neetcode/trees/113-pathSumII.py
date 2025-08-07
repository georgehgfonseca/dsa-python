# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(root, path, currSum):
            if not root:
                return

            path.append(root.val)
            currSum += root.val

            isLeaf = not root.right and not root.left
            if isLeaf and currSum == targetSum:
                res.append(path[:])
            
            dfs(root.left, path, currSum)
            dfs(root.right, path, currSum)
            path.pop()
        
        dfs(root, [], 0)
        return res