from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(root, parent, isLeftChild):
            if not root:
                return
            if not root.left and not root.right:
                if root.val == target:
                    if parent.val == target:
                        self.mustCheckLeaves = True
                    if isLeftChild:
                        parent.left = None
                    else:
                        parent.right = None
                return
            
            dfs(root.left, root, True)
            dfs(root.right, root, False)
        
        if not root:
            return root
        
        self.mustCheckLeaves = True
        while self.mustCheckLeaves:
            self.mustCheckLeaves = False
            if not root.left and not root.right and root.val == target:
                return None
            dfs(root.left, root, True)
            dfs(root.right, root, False)
        
        return root


      

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
    (tree0, 3), 
    (tree1, 3), 
    (tree2, 3), 
    (tree3, 3), 
]

s = Solution()
for t in testCases:
    print(s.removeLeafNodes(t[0], t[1]))


# s = "abc"
# s = s.replace("a", "A")
# print(s)

# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# print(queue)
# for elem in queue:
#     print(elem)
# for i in range(len(queue)):
#     print(i)