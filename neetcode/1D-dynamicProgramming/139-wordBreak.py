class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s               = "neetcode"
        # i               =  *
        # word            = "neet"
        # j               =     *
        # matched         = True
        memo = {len(s) : True}

        def helper(i):
            if i in memo:
                return memo[i]

            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i + len(word)] == word:
                    if helper(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return helper(0)

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        # s               = "neetcode"
        # i               =  *
        # word            = "neet"
        # j               =     *
        # matched         = True
        self.res = False
        def helper(i):
            if i >= len(s):
                self.res = True
                return

            for word in wordDict:
                matched = True
                for j in range(len(word)):
                    if i+j >= len(s) or s[i+j] != word[j]:
                        matched = False
                        break
                if matched:
                    helper(i+j+1)
        helper(0)
        return self.res


    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # s               = "neetcode"
        # wordStartI      =  *
        # currI           =   *
        # checkedI        =   *
        # possible        = ["neet"]
        # nextPossible    = []

        self.res = False
        def helper(wordStartI, currI, possibleMatches):
            if currI >= len(s):
                self.res = True
                return
            if not possibleMatches:
                return
            
            # if a match, eval using the match or skipping it
            checkedIdx = currI - wordStartI
            nextPossibleMatches = []
            for word in possibleMatches:
                if checkedIdx < len(word) and word[checkedIdx] == s[currI]:
                    nextPossibleMatches.append(word)
                    if checkedIdx == len(word) - 1:
                        # a complete match has been found
                        helper(currI + 1, currI + 1, wordDict)
            # check possible matches without using one
            helper(wordStartI, currI + 1, nextPossibleMatches)
        
        helper(0, 0, wordDict)
        return self.res
            

            
        