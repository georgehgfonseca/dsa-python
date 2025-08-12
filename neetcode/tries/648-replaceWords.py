class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

    def addWord(self, word):
        curr = self
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isWord = True

    def search(self, word):
        curr = self
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.isWord

    def searchRoot(self, word):
        curr = self
        idx = 0
        res = 0
        for letter in word:
            if letter not in curr.children:
                return res
            curr = curr.children[letter]
            idx += 1
            if curr.isWord:
                return idx
        return res


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieNode()
        for word in dictionary:
            trie.addWord(word)

        words = sentence.split(" ")
        res = []
        for word in words:
            rootIdx = trie.searchRoot(word)
            if rootIdx == 0:
                res.append(word)
            else:
                res.append(word[:rootIdx])
        return " ".join(res)

