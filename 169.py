from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        res = None
        mp = {}
        for i in nums:
            if mp.get(i, 0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1
                if mp[i] > len(nums) // 2:
                    res = mp[i]
                    break
        return res

