from typing import List

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

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # brute force
        words = sentence.split()
        res = ""
        for word in words:
            matched = False
            for key in dictionary:
                if key in word:
                    res += key + " "
                    matched = True
                    break
            if not matched:
                res += word + " "

        return res

testCases = [
    (["cat","bat","rat"], "the cattle was rattled by the battery"), 
    (["a","b","c"], "aadsfasf absbs bbab cadsfafs"), 
]

s = Solution()
for t in testCases:
    print(s.replaceWords(t[0], t[1]))