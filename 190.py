class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 0
        while count < 32:
            res <<= 1
            res |= (n & 1)
            n >>= 1
            count += 1
        return res
