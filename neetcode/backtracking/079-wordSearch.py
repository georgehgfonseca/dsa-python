from typing import List

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(i, j, wordIndex, visited):
            if i == -1 or j == -1 or i > len(board) - 1 or j > len(board[i]) - 1:
                # invalid cell
                return False
            if board[i][j] != word[wordIndex]:
                return False
            if visited and (i, j) in visited:
                # repeated cell
                return False
            if wordIndex + 1 == len(word):
                # found the whole word (should not expand)
                return True 
            
            visited.add((i, j))
            # expand to next char
            left = search(i-1, j, wordIndex+1, visited.copy())
            right = search(i+1, j, wordIndex+1, visited.copy())
            down = search(i, j-1, wordIndex+1, visited.copy())
            up = search(i, j+1, wordIndex+1, visited.copy())
            return left or right or down or up
        
        if len(board) * len(board[0]) < len(word):
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(i, j, 0, set()):
                    return True
        return False
        

testCases = [
    ([["A","B","C","E"], # True
     ["S","F","C","S"],
     ["A","D","E","E"]], "ABCCED"),
    ([["A","B","C","E"], # False
      ["S","F","C","S"],
      ["A","D","E","E"]], "ABCB"),
    ([["a","a","a","a"], # False
      ["a","a","a","a"],
      ["a","a","a","a"]], "aaaaaaaaaaaaa"),
    ([["a","a","b","a","a","b"], # False
      ["a","a","b","b","b","a"],
      ["a","a","a","a","b","a"],
      ["b","a","b","b","a","b"],
      ["a","b","b","a","b","a"],
      ["b","a","a","a","a","b"]], "bbbaabbbbbab")
]

s = Solution()
for t in testCases:
    print(s.exist(t[0], t[1]))