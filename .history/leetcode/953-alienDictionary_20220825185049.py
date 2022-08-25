from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                idxs = []
                for k in range(len(words)):
                    if order[i:j] == words[k][0 : j - i]:
                        if len(idxs) == 0:
                            idxs.append(k)
                        else:
                            if idxs[-1] > k:
                                return False

        return True


testCases = [(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")]
s = Solution()
for t in testCases:
    print(s.isAlienSorted(t[0], t[1]))
