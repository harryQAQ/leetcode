from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash
        # mp = {}
        # for i in nums:
        #     if i not in mp:
        #         mp[i] = 1
        #     else:
        #         mp[i] -= 1
        # for k, v in mp.items():
        #     if v == 1:
        #         return k
        #异或
        res = nums[0]

        for i in range(1, len(nums)):
            res ^= nums[i]
        return res 