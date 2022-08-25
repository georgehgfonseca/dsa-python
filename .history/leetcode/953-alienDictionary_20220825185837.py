from operator import indexOf
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True
        for i in range(len(words) - 1):
            # compare i-th word with i+1-th word
            for j in range(1, len(words[i])):
                idxI = order.indexOf(words[i][0:j])
                idxI1 = order.indexOf(words[i + 1][0:j])
                if idxI > idxI1:
                    return False
                elif idxI < idxI1:
                    break
        return True

        # for i in range(len(order)):
        #     for j in range(i + 1, len(order)):
        #         idxs = []
        #         for k in range(len(words)):
        #             if order[i:j] == words[k][0 : j - i]:
        #                 if len(idxs) == 0:
        #                     idxs.append(k)
        #                 else:
        #                     if idxs[-1] > k:
        #                         return False

        # return True


testCases = [(["hello", "leetcode"], "lhabcdefgijkmnopqrstuvwxyz")]
s = Solution()
for t in testCases:
    print(s.isAlienSorted(t[0], t[1]))
