class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    # TODO had to look at the solution - my trie was using an array of children instead

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.word
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
            elif word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            return False
        
        return dfs(self.root, 0)
