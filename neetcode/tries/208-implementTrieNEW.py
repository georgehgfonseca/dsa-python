class TrieNode:

    def __init__(self, letter=None, children={}, is_end_of_word=False):
        self.letter = letter
        self.children = children
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode(None, {}, False)
        

    def insert(self, word: str) -> None:
        node_ref = self.root
        for i in range(len(word)):
            if word[i] not in node_ref.children:
                # add it to children if it doesn't exist
                node_ref.children[word[i]] = TrieNode(word[i], {}, False)

            # move to its child to add new letters
            node_ref = node_ref.children[word[i]]

        node_ref.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        node_ref = self.root

        for i in range(len(word)):
            if word[i] in node_ref.children:
                if i == len(word) - 1 and node_ref.children[word[i]].is_end_of_word:
                    return True
                node_ref = node_ref.children[word[i]]
            else:
                return False

        return False
        

    def startsWith(self, prefix: str) -> bool:
        if not self.root.children:
            return False

        node_ref = self.root

        for i in range(len(prefix)):
            if prefix[i] in node_ref.children:
                node_ref = node_ref.children[prefix[i]]
            else:
                return False

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

print("===================")
obj = Trie()
print(obj.startsWith("a"))
