from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        LIS = [1  for _ in range(n)]
        LIS[1] = 1
        res = 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[j] + 1, LIS[i])
            if LIS[i] > res: 
                res = LIS[i]
        return res

x = Solution()
print(x.lengthOfLIS([-2,-1]))