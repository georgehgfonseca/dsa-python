class Solution:
    def getSum(self, a: int, b: int) -> int:
        # TODO: does not work with negative nums
        res = 0
        i = 0
        while a or b:
            bitA = a & 1
            bitB = b & 1
            a >>= 1
            b >>= 1
            if bitA and bitB:
                res += 2 ** (i + 1)
            elif bitA or bitB:
                res += 2 ** i
            i += 1
        return res

    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # 32-bit mask
        MAX_INT = 0x7FFFFFFF
        
        # convert to unsigned 32-bit representation
        a &= MASK
        b &= MASK
        
        res = 0
        i = 0
        while a or b:
            bitA = a & 1
            bitB = b & 1
            a = (a >> 1) & MASK
            b = (b >> 1) & MASK
            if bitA and bitB:
                res += 1 << (i + 1)
            elif bitA or bitB:
                res += 1 << i
            i += 1
        
        # convert back to signed integer
        return res if res <= MAX_INT else ~(res ^ MASK)


    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)