from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        #每一位算有几个
        for i in range(32):
            cnt = 0
            bit = 1 << i
            for num in nums:
                if num & bit:
                    cnt += 1
            if cnt % 3:
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res 