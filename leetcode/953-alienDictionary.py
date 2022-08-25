from operator import indexOf
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True
        # to make searches in order faster O(1)
        orderDict = {char: order.find(char) for char in order}
        for i in range(len(words) - 1):
            # compare i-th word with i+1-th word
            samePrefix = True
            for j in range(0, min(len(words[i]), len(words[i + 1]))):
                idxI = orderDict[words[i][j]]
                idxI1 = orderDict[words[i + 1][j]]
                if idxI > idxI1:
                    return False
                elif idxI < idxI1:
                    samePrefix = False
                    break
            # words i and i+1 have the same prefix
            if samePrefix and len(words[i]) > len(words[i + 1]):
                return False
        return True


testCases = [
    (["apple", "app"], "abcdefghijklmnopqrstuvwxyz"),
    (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
    (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
]
s = Solution()
for t in testCases:
    print(s.isAlienSorted(t[0], t[1]))
