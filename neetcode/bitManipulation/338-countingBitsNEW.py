class Solution:
    def countBits(self, n: int) -> List[int]:
        # TODO: had to look at the O(n) solution
        cache = [0]
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            cache.append(1 + cache[i - offset])
        return cache

    def countBits2(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            while i:
                count += i % 2
                i >>= 1
            res.append(count)
        return res