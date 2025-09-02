class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key= lambda x : (-len(x), x))
        for word in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                if j == len(word):
                    return word
       
        return ""
            

    def findLongestWordWOSort(self, s: str, dictionary: List[str]) -> str:
        maxMatch = ""
        for word in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                if j == len(word):
                    if len(word) > len(maxMatch) or (len(word) == len(maxMatch) and word < maxMatch):
                        maxMatch = word
                    break
       
        return maxMatch
            




    def findLongestWordTL(self, s: str, dictionary: List[str]) -> str:
        # backtracking - decision: delete current char or not
        # udapte dictionary candidate matches
        # base-case: idx >= len(s) or no match candidate
        # s = "abcadsa" dict = ["casa", "cada", "cama"] -> "cada"
        # s = "abcaa" dict = ["casa", "cada", "cama"] -> ""
        # s = "abcasaaa" dict = ["casa", "cada", "cama"] -> "casa"
        # opt: use a trie to keep track of candidates (?)
        dictionary.sort()
        self.maxMatch = ""
        def dfs(i, curr, cands):
            if not cands:
                return
            
            nextCands = []
            for cand in cands:
                if len(cand) < len(curr):
                    continue
                if cand[:len(curr)] == curr:
                    if len(cand) == len(curr) and (len(curr) > len(self.maxMatch) or (len(curr) == len(self.maxMatch) and curr < self.maxMatch)):
                        self.maxMatch = curr
                        continue                        
                    nextCands.append(cand)
            if i + 1 >= len(s):
                return

            dfs(i + 1, curr + s[i + 1], nextCands)
            dfs(i + 1, curr, nextCands)
        
        dfs(-1, "", dictionary)
        return self.maxMatch



