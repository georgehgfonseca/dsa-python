class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.trie = self.root
        
    # word: apple
    # sub:  app
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        if len(self.root.children) == 0:
            return False

        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj.startsWith("a"))
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("bee"))
print(obj.startsWith("app"))
print(obj.startsWith("apple"))
obj.insert("app")
print(obj.search("app"))
