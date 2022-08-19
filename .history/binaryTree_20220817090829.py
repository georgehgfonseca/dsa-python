class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traversePreorder(self, root):
        res = []
        self.helperPreorder(root, res)
        return res

    def traverseOrder(self, root):
        res = []
        self.helperOrder(root, res)
        return res

    def traversePostorder(self, root):
        res = []
        self.helperPostorder(root, res)
        return res

    def helperPreorder(self, root, res):
        if root is not None:
            res.append(root.val)
            self.helperPreorder(root.left, res)
            self.helperPreorder(root.right, res)

    def helperOrder(self, root, res):
        if root is not None:
            self.helperOrder(root.left, res)
            res.append(root.val)
            self.helperOrder(root.right, res)

    def helperPostorder(self, root, res):
        if root is not None:
            self.helperPostorder(root.left, res)
            self.helperPostorder(root.right, res)
            res.append(root.val)

    def addNode(self, root, val):
        if root is None:
            root = TreeNode(val)
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.addNode(root.left, val)
        elif val == root.val:
            return
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.addNode(root.right, val)


class TreeOperations:
    def canMerge(self, trees: list[TreeNode]) -> list[TreeNode]:
        if len(trees) == 1:
            return trees[0]

        for i in range(len(trees)):
            print(trees[i].traversePreorder(trees[i]))
            for j in range(i + 1, len(trees)):
                self.traverseAndMerge(trees[i], trees[j])
                # self.traverseAndAdd(trees[i], res)
                # trees.pop(i)

        # res = copy.deepcopy(trees[0])
        # for i in range(1, len(trees)):
        #     self.traverseAndAdd(trees[i], res)
        for tree in trees:
            print(tree.traversePreorder(tree))
            if tree.left is not None and tree.right is not None:
                return tree

    def traverseAndMerge(self, root1, root2):
        """ "Return True iif any node at a tree (root) is the root of another tree (equals val)"""
        if root1 != None:
            if root1 == root2.val:
                root1.left = root2.left
                root1.right = root2.right
                # root2.left = None
                # root2.right = None
            else:
                self.traverseAndAdd(root1.left, root2)
                self.traverseAndAdd(root1.right, root2)

    def traverseAndCheck(self, root, val):
        """ "Return True iif any node at a tree (root) is the root of another tree (equals val)"""
        if root != None:
            if root == val:
                return True
            else:
                self.traverseAndAdd(root.left, val)
                self.traverseAndAdd(root.right, val)
        return False

    def traverseAndAdd(self, root, res):
        if root != None:
            self.traverseAndAdd(root.left, res)
            self.addNode(res, root.val)
            self.traverseAndAdd(root.right, res)
