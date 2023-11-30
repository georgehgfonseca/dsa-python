from typing import List, Optional

# premium problem available in https://leetcode.ca/all/156.html
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # TODO: copied solution
        if root is None or root.left is None:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return new_root

        # father = {}
        # left_backup = {}

        # root_ref = root
        # prev_node = root
        # while root:
        #     left_backup[root] = root.left
        #     root = root.left
        #     father[root.left] = prev_node

        # while root_ref:
        #     root_ref = root_ref.left
        #     prev_node = root


        # newNode = root
        # while newNode:
        #     temp = newNode
        #     newNode = root.left
        #     newNode.left = temp
        #     newNode.right = temp.right
        
        return newNode



t = TreeNode(1, 
             TreeNode(2, 
                      TreeNode(4), 
                      TreeNode(5)), 
             TreeNode(3))
testCases = [t]
s = Solution()
for t in testCases:
    print(s.upsideDownBinaryTree(t))
