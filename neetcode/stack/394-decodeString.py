class Solution:
    def decodeString(self, s: str) -> str:
        # when read a "[" starts stacking
        # when read a "]" de-stack
        # a stack for the numbers
        # s               = 3[a2[c]]
        # i               = *
        # numberStack     = [3]
        # letterBuffer    = []
        # stackNextLetter = False
        # res             = ""
        numberStack = []
        letterStack = []
        res = ""
        i = 0
        while i < len(s):
            if ord("a") <= ord(s[i]) <= ord("z"): 
                if not letterStack:
                    res += s[i]
                else:
                    letterStack[-1] += s[i]
            elif s[i] == "[":
                letterStack.append("")
            elif s[i] == "]":
                letters = numberStack.pop() * letterStack.pop()
                if letterStack:
                    letterStack[-1] += letters
                else:
                    res += letters
            else:
                # read an integer
                num = s[i]
                j = i + 1
                while j < len(s) and ord("0") <= ord(s[j]) <= ord("9"):
                    num += s[j]
                    j += 1
                i = j - 1
                numberStack.append(int(num))
            i += 1
        return res