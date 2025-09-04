from typing import List, Set
import collections

class Solution:
    def validSquare(self, words: List[str]):
        wordIdx = {(word, i) for i, word in enumerate(words)}
        for i in range(len(words)):
            word = ""
            for j in range(len(words)):
                word += words[j][i]
            if (word, i) not in wordIdx:
                return False
        return True
    
    def getWordsFromIdxs(self, words, idxs):
        res = []
        for idx in idxs:
            res.append(words[idx])
        return res


    def find_word_squares(self, words: List[str]) -> List[List[str]]:
        # assuming all words have the same size
        # try all word order permutations
        squareSize = len(words[0])
        res = []
        def dfs(currIdxs, currIdxsSet):
            if len(currIdxs) == squareSize:
                currSquare = self.getWordsFromIdxs(words, currIdxs)
                if self.validSquare(currSquare):
                    res.append(currSquare)
                return
            
            for idx in range(len(words)):
                if idx not in currIdxsSet:
                    currIdxsSet.add(idx)
                    currIdxs.append(idx)
                    dfs(currIdxs, currIdxsSet)
                    currIdxs.pop()
                    currIdxsSet.remove(idx)

        dfs([], set())
        return res

    def find_word_squares(self, words):
        res = []
        # Preprocess words: O(#words * word-length) time and space
        words_by_letter_position = collections.defaultdict(set)
        for word in words:
            for index, letter in enumerate(word):
                words_by_letter_position[(index, letter)].add(word)

        for word in words:
            # Initialize a set of incomplete possible squares
            possible_squares = set([(word,)])

            # As long as we have any incomplete squares:
            while possible_squares:
                square = possible_squares.pop()
                # Find all candidate words that can extend this square
                keys = [(i, square[i][len(square)]) for i in range(len(square))]
                possible_matches = [words_by_letter_position[key] for key in keys]

                for valid_word in set.intersection(*possible_matches):
                    valid_square = square + (valid_word,)
                    if len(valid_square) == len(word):
                        res.append(valid_square)
                    else:
                        possible_squares.add(valid_square)

        return res

testCases = [["BALL", "AREA", "LEAD", "LADY", "DEAR", "YARD"]] # [["BALL", "AREA", "LEAD", "LADY"], ["LADY", "AREA", "DEAR", "YARD"]]
s = Solution()
for t in testCases:
    print(s.find_word_squares(t))
