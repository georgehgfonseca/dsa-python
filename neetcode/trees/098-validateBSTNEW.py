from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, max_children, min_children):
            if not root:
                return True
            
            if root.val >= max_children or root.val <= min_children:
                return False

            if root.left and root.right:
                if root.left.val >= root.right.val:
                    return False
                return helper(root.left, root.val, min_children) and helper(root.right, max_children, root.val)

            if root.left and not root.right:
                if root.left.val >= root.val:
                    return False
                return helper(root.left, root.val, min_children)

            if root.right and not root.left:
                if root.right.val <= root.val:
                    return False
                return helper(root.right, max_children, root.val)

            return True
            
        return helper(root, float("inf"), float("-inf"))

      

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
    tree0, # True
    tree1, # True
    tree2, # False
    tree3, # False
]

s = Solution()
for t in testCases:
    print(s.isValidBST(t))


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