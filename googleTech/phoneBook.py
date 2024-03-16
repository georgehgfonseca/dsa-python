from typing import List

class Solution:

    def phoneBook(self, n: int, entries: List[str], queries: List[str]):
        name_phone_map = {}
        for entry in entries:
            data = entry.split()
            name, phone = data[0], data[1]
            name_phone_map[name] = phone
        
        res = ""
        for query in queries:
            if query in name_phone_map:
                res += query + "=" + name_phone_map[query] + "\n"
            else:
                res += "Not found\n"

        return res

testCases = [(3, ["sam 99912222", "tom 11122222", "harry 12299933"], ["sam", "edward", "harry"])]

s = Solution()
for t in testCases:
    print(s.phoneBook(t[0], t[1], t[2]))