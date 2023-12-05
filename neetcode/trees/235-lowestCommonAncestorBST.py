from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # enumerate the ancestors of p and q
        self.ancestors_p = list()
        def get_ancestors_p(root, p, curr_path):
            if root:
                curr_path.append(root)
                if root == p:
                    for node in curr_path:
                        self.ancestors_p.insert(0, node)
                    return
                get_ancestors_p(root.left, p, curr_path.copy())
                get_ancestors_p(root.right, p, curr_path.copy())
        
        self.ancestors_q = list()
        def get_ancestors_q(root, q, curr_path):
            if root:
                curr_path.append(root)
                if root == q:
                    for node in curr_path:
                        self.ancestors_q.insert(0, node)
                    return
                get_ancestors_q(root.left, q, curr_path.copy())
                get_ancestors_q(root.right, q, curr_path.copy())
        
        get_ancestors_p(root, p, [])
        get_ancestors_q(root, q, [])

        for ancestor_p in self.ancestors_p:
            for ancestor_q in self.ancestors_q:
                if ancestor_p == ancestor_q:
                    return ancestor_p



tree1 = TreeNode(1, 
                 TreeNode(2), 
                 TreeNode(3))
tree2 = TreeNode(1, 
                 TreeNode(2), 
                 TreeNode(3))
tree3 = TreeNode(1, 
                 TreeNode(2), 
                 None)
tree4 = TreeNode(1, 
                 None, 
                 TreeNode(2))

testCases = [
    (tree1, tree2), # True
    (tree3, tree4)  # False
]

s = Solution()
for t in testCases:
    print(s.isSameTree(t[0], t[1]))