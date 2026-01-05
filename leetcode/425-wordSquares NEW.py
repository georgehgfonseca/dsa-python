from typing import List
import time


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.wordsWithPrefix = []  # suggested by chatGPT

    def add(self, word):
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
            root.wordsWithPrefix.append(word)

    def subWordSearch(self, word):
        root = self
        for char in word:
            if char not in root.children:
                return []
            root = root.children[char]
        return root.wordsWithPrefix


class Solution:
    def find_word_squares_improved(self, words: List[str]):
        # with hints from chatGPT
        res = []
        wordSize = len(words[0])

        trie = TrieNode()
        for word in words:
            trie.add(word)

        def dfs(step, curr):
            if len(curr) == wordSize:
                res.append(curr.copy())
                return

            prefix = "".join(word[step] for word in curr)

            for cand in trie.subWordSearch(prefix):
                curr.append(cand)
                dfs(step + 1, curr)
                curr.pop()

        for word in words:
            dfs(1, [word])

        return res

    def find_word_squares(self, words: List[str]):
        # include each word as a row for each
        # try all combinations - prune some of them
        # keep track of curr matches for each column (when no match, move to next combination)
        res = []
        wordSize = len(words[0])

        trie = TrieNode()
        for word in words:
            trie.add(word)

        def dfs(curr):
            if len(curr) == wordSize:
                res.append(curr.copy())
                return

            for word in words:
                # check weather curr is valid after adding word to it
                curr.append(word)
                valid = True

                for j in range(wordSize):
                    partial = []
                    for i in range(len(curr)):
                        partial.append(curr[i][j])

                    # is there a match for partial?
                    if not trie.subWordSearch("".join(partial)):
                        valid = False
                        break

                if valid:
                    dfs(curr)
                curr.pop()

        dfs([])
        return res


start = time.time()
testCases = [
    ["BALL", "AREA", "LEAD", "LADY", "DEAR", "YARD"]
]  # [["BALL", "AREA", "LEAD", "LADY"], ["LADY", "AREA", "DEAR", "YARD"]]
s = Solution()
for t in testCases:
    print(s.find_word_squares_improved(t))
print(f"wall time: {time.time() - start}")


# ORGINAL
# is there a way to optimize this:

from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

    def add(self, word):
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]

        root.isWord = True

    def subWordSearch(self, word):
        root = self
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return True


class Solution:
    def find_word_squares(self, words: List[str]):
        # include each word as a row for each
        # try all combinations - prune some of them
        # keep track of curr matches for each column (when no match, move to next combination)
        res = []
        wordSize = len(words[0])

        trie = TrieNode()
        for word in words:
            trie.add(word)

        def dfs(remainingWords, curr):
            if len(curr) == wordSize:
                res.append(curr.copy())
                return

            for word in remainingWords:
                # check weather curr is valid after adding word to it
                curr.append(word)
                valid = True

                for j in range(wordSize):
                    partial = ""
                    for i in range(len(curr)):
                        partial += curr[i][j]

                    # is there a match for partial?
                    if not trie.subWordSearch(partial):
                        valid = False
                        break

                if valid:
                    remainingWordsCopy = remainingWords.copy()
                    remainingWordsCopy.remove(word)
                    dfs(remainingWordsCopy, curr)
                curr.pop()

        dfs(set(words), list())
        return res


start = time.time()
testCases = [
    ["BALL", "AREA", "LEAD", "LADY", "DEAR", "YARD"]
]  # [["BALL", "AREA", "LEAD", "LADY"], ["LADY", "AREA", "DEAR", "YARD"]]
s = Solution()
for t in testCases:
    print(s.find_word_squares(t))
print(f"wall time: {time.time() - start}")
