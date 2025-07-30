class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

    def addWord(self, word):
        currNode = self
        for i in range(len(word)):
            if word[i] not in currNode.children:
                currNode.children[word[i]] = TrieNode()
            currNode = currNode.children[word[i]]
        currNode.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create a trie on the words
        trie = TrieNode()
        for w in words:
            trie.addWord(w)

        # iterate over each starting cell and add the words found from it on the res 
        res = set()
        visited = set()

        def dfs(i, j, node, currWord):
            outOfBounds = i < 0 or j < 0 or i >= len(board) or j >= len(board[i])
            if outOfBounds or (i, j) in visited or board[i][j] not in node.children:
                return

            visited.add((i, j))
            node = node.children[board[i][j]]
            currWord += board[i][j]
            if node.isWord:
                res.add(currWord)

            dfs(i - 1, j, node, currWord)
            dfs(i + 1, j, node, currWord)
            dfs(i, j - 1, node, currWord)
            dfs(i, j + 1, node, currWord)
            visited.remove((i, j))


        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, trie, "")
        
        return list(res)


    def findWordsTL(self, board: List[List[str]], words: List[str]) -> List[str]:
        # search in graphs

        def getValidNeighbors(i, j, index):
            neighbors = set()
            if i + 1 < len(board) and board[i + 1][j] == word[index] and (i + 1, j) not in self.visited:
                neighbors.add((i + 1, j))
            if j + 1 < len(board[i]) and board[i][j + 1] == word[index] and (i, j + 1) not in self.visited:
                neighbors.add((i, j + 1))
            if i - 1 >= 0 and board[i - 1][j] == word[index] and (i - 1, j) not in self.visited:
                neighbors.add((i - 1, j))
            if j - 1 >= 0 and board[i][j - 1] == word[index] and (i, j - 1) not in self.visited:
                neighbors.add((i, j - 1))
            return neighbors


        def dfs(i, j, index, word):
            #print(f"node ({i},{j}) curr {board[i][j]} nextIdx {index}", end="")
            if index >= len(word):
                # matched the whole word
                #print("  FOUND!")
                return True
            neighbors = getValidNeighbors(i, j, index)
            #print(f" neigh: {neighbors}")

            if not neighbors:
                #print("  STOP!!")
                return False

            anyPath = False
            for (neiI, neiJ) in neighbors:
                self.visited.add((neiI, neiJ))
                foundPath = dfs(neiI, neiJ, index + 1, word)
                self.visited.discard((neiI, neiJ))
                if foundPath:
                    anyPath = True
            
            return anyPath

        res = []
        for word in words:
            hasWord = False
            self.visited = set()
            for i in range(len(board)):
                for j in range(len(board[i])):
                    self.visited.add((i, j))
                    if board[i][j] == word[0] and dfs(i, j, 1, word):
                        hasWord = True
                        break
                    self.visited.remove((i, j))
                if hasWord:
                    break

            if hasWord:
                res.append(word)
        return res