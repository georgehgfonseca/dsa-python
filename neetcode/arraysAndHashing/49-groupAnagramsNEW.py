from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_letters_map = dict()
        for word in strs:
            word_letters_map[word] = dict()
            for letter in word:
                if letter not in word_letters_map[word]:
                    word_letters_map[word][letter] = 1
                else:
                    word_letters_map[word][letter] += 1
        groupings = []
        i = 0
        while i < len(strs):
            groupings.append([strs[i]])
            j = i + 1
            while j < len(strs):
                if word_letters_map[strs[i]] == word_letters_map[strs[j]]:
                    groupings[i].append(strs[j])
                    strs.pop(j)
                    j -= 1
                j += 1
            i += 1
        return groupings




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