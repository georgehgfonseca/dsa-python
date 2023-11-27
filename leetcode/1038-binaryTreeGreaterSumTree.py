from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        # Traverse tree and save vals
        def traverse(root, vals):
            if root:
                vals.append(root.val)
                traverse(root.left, vals)
                traverse(root.right, vals)

        vals = []
        traverse(root, vals)

        # Compute the output for each node
        val_output = {}
        for val in vals:
            val_output[val] = val
            for val2 in vals:
                if val2 > val:
                    val_output[val] += val2

        # Replace nodes according to the val_output map
        def traverse_and_replace(root, val_output):
            if root:
                root.val = val_output[root.val]
                traverse_and_replace(root.left, val_output)
                traverse_and_replace(root.right, val_output)


        traverse_and_replace(root, val_output)

        return root
            


t = TreeNode(4, 
             TreeNode(1, 
                      TreeNode(0), 
                      TreeNode(2, 
                               None, 
                               TreeNode(3))), 
             TreeNode(6, 
                      TreeNode(5),
                      TreeNode(7, 
                               None,
                               TreeNode(8))))

testCases = [t]
s = Solution()
for t in testCases:
    print(s.bstToGst(t))
