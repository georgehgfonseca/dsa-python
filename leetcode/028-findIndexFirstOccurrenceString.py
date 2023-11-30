

class Solution:
  
    def findIndexFirstOccurrence(self, haystack: str, needle: str) -> int:
        # TODO: copied solution
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Main algorithm
        n = 0 #needle index
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1
    
        # O(m * n) time complexity (can be improved)
        # for i in range(len(haystack)):
        #     if haystack[i] == needle[0] and i + len(needle) - 1 < len(haystack):
        #         found = True
        #         for j in range(len(needle)):
        #             if haystack[i + j] != needle[j]:
        #                 found = False
        #                 break
        #         if found:
        #             return i
        # return -1


t1 = ("sadbutsad", "sad") # 0
t2 = ("leetcode", "leeto") # -1
t3 = ("llle", "lle") # 1
t4 = ("lllel", "elee") # -1
t5 = ("", "k") # -1
t6 = ("asdfgh", "gh") # 4
testCases = [t1, t2, t3, t4, t5, t6]

s = Solution()
for t in testCases:
    print(s.findIndexFirstOccurrence(t[0], t[1]))