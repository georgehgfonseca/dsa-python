from typing import List
from types import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        
        word_letter_count = dict()
        for word in strs:
            # handling duplicates
            if word in word_letter_count:
                continue

            word_letter_count[word] = dict()
            for letter in word:
                if letter not in word_letter_count[word]:
                    word_letter_count[word][letter] = 1
                else:
                    word_letter_count[word][letter] += 1
        
        ans = []
        added = [False for _ in strs]
        for i in range(len(strs)):
            if added[i]:
                continue
            word1 = strs[i]
            ans.append([word1])
            added[i] = True

            # add duplicates together with word1
            for j in range(i + 1, len(strs)):
                if added[j]:
                    continue

                word2 = strs[j]
                if word_letter_count[word1] == word_letter_count[word2]:
                    ans[-1].append(word2)
                    added[j] = True

        return ans


test_cases = [
    ["tea","","eat","","tea",""],          # [["","",""],["eat","tea","tea"]]
    ["",""],                               # [["", ""]]
    ["eat","tea","tan","ate","nat","bat"], # [["bat"],["nat","tan"],["ate","eat","tea"]]
    [""],                                  # [[""]]
    ["aba", "aab", "cab", "bac", "aaa"],   # [["aba", "aab"], ["cab", "bac"], ["aaa"]]
]
s = Solution()
for t in test_cases:
    print(s.groupAnagrams(t))