class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        visitedSet = set()
        deadendsSet = set(deadends)

        queue = deque([("0000", 0)])
        while queue:
            (code, hops) = queue.popleft()
            if code in deadendsSet or code in visitedSet:
                continue
            if code == target:
                return hops
            visitedSet.add(code)

            for i in range(4):
                digit = int(code[i])
                for move in [-1, 1]:
                    newDigit = (digit + move) % 10
                    newCode = code[:i] + str(newDigit) + code[i + 1:]
                    queue.append((newCode, hops + 1))
        
        return -1
