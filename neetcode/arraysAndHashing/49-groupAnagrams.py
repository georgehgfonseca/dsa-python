from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            char_count = [0] * 26
            for letter in str:
                char_count[ord(letter) - ord("a")] += 1
            
            tuple_char_count = tuple(char_count)

            if tuple_char_count in anagrams:
                anagrams[tuple_char_count].append(str)
            else:
                anagrams[tuple_char_count] = [str]

        output = []
        for anagram in anagrams:
            output.append(anagrams[anagram])
        return output


        # # Accepatable but yet not optimal (O(m * n log(n)))
        # # sort each string
        # strs_sorted = []
        # for i in range(len(strs)):
        #     strs_sorted.append(''.join(sorted(strs[i])))

        # # group the indexes of equal strings 
        # groupings_strs = []
        # groupings_indexes = []
        # processed_indexes = set()
        # for i in range(len(strs_sorted)):
        #     if i in processed_indexes:
        #         continue

        #     processed_indexes.add(i)
        #     curr_grouping = [i]
        #     curr_grouping_str = [strs[i]]
        #     for j in range(i + 1, len(strs_sorted)):
        #         if j in processed_indexes:
        #             continue
                
        #         strs_are_anagrams = strs_sorted[i] == strs_sorted[j]
                
        #         if strs_are_anagrams:
        #             curr_grouping.append(j)
        #             curr_grouping_str.append(strs[j])
        #             processed_indexes.add(j)

        #     groupings_indexes.append(curr_grouping)
        #     groupings_strs.append(curr_grouping_str)
        
        # return groupings_strs

        # Time Limit Exceeded
        # letter_occurencies_map = {}

        # for str in strs:
        #     if str in letter_occurencies_map:
        #         continue

        #     letter_occurencies_map[str] = {}
            
        #     for letter in str:
        #         if letter not in letter_occurencies_map[str]:
        #             letter_occurencies_map[str][letter] = 1
        #         else:
        #             letter_occurencies_map[str][letter] += 1
        
        # groupings = []
        # grouped_indexes = []
        # for i in range(len(strs)):
        #     if i in grouped_indexes:
        #         continue

        #     curr_grouping = [strs[i]]
        #     grouped_indexes.append(i)
        #     for j in range(i + 1, len(strs)):
        #         if j in grouped_indexes:
        #             continue
        #         if len(strs[j]) != len(strs[i]):
        #             continue
                    
        #         group_strs = True
        #         for letter in letter_occurencies_map[strs[j]]:
        #             if letter not in letter_occurencies_map[strs[i]]:
        #                 group_strs = False
        #                 break
        #             if letter_occurencies_map[strs[j]][letter] != letter_occurencies_map[strs[i]][letter]:
        #                 group_strs = False
        #                 break
        #         if group_strs:
        #             curr_grouping.append(strs[j])
        #             grouped_indexes.append(j)
        #     groupings.append(curr_grouping)
        
        # return groupings
               


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