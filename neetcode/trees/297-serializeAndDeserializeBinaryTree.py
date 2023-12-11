from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data:str) -> Optional[TreeNode]:
        nodes = data.split(",")

        self.i = 0
        
        def dfs():
            if nodes[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(nodes[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()


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

c = Codec()
print(c.serialize(tree0))
print(c.deserialize(c.serialize(tree0)))
