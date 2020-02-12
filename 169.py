from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1: return nums[0]
        res = None
        mp = {}
        for i in nums:
            if mp.get(i, 0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1
                if mp[i] > l // 2:
                    res = i
                    break
        return res

