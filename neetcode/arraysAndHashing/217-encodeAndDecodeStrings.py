from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            encoded += f"{len(str)}#{str}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        curr_num = ""
        while i < len(s):
            if s[i] != "#":
                curr_num += s[i]
                i += 1
            else:
                str_length = int(curr_num)
                decoded.append(s[i + 1:i + 1 + str_length])
                i += str_length + 1
                curr_num = ""

        return decoded



test_cases = [["leet", "code"], 
              # 4#leet4#code
              # i =1
              # s[i] = #
              # curr_num = ""
              # str_length = 4
              # decoded = [""]
              
              ["work", "hard", "play", "hard"],
              ["4#wo4#rk", "4#hard", "pl#$21ay", "hard"]]
s = Codec()
for t in test_cases:
    print(s.decode(s.encode(t)))

