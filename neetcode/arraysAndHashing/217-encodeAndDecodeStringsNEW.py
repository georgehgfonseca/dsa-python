from typing import List


class Codec:

    def encode(self, strs: List[str]) -> str:
        # add some prefix to each string with the number of chars of each str
        # ["neet","code","love","you"] -> \4\neet\4\code\4\love\3\you
        output = ""
        for str in strs:
            output += f"|{len(str)}|{str}"
        return output

    def decode(self, s: str) -> List[str]:
        # read a char, if it is the marker, read the number n, then the ending marker, then n chars of the string
        output = []
        i = 0
        while i < len(s):
            if s[i] == "|":
                i += 1
                currNumStr = ""
                while s[i] != "|":
                    currNumStr += s[i]
                    i += 1
                currNum = int(currNumStr)
                output.append(s[i + 1 : i + currNum + 1])
                i += currNum
            i += 1
        return output


test_cases = [
    ["leet", "code"],
    # 4#leet4#code
    # i =1
    # s[i] = #
    # curr_num = ""
    # str_length = 4
    # decoded = [""]
    ["work", "hard", "play", "hard"],
    ["4#wo4#rk", "4#hard", "pl#$21ay", "hard"],
]
s = Codec()
for t in test_cases:
    print(s.decode(s.encode(t)))
