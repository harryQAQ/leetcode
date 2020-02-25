from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]

        dp[0][0], dp[0][1] = nums[0], nums[0]
        res = 0
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            res = max(res, dp[i][0])
        return res

x = Solution()
print(x.maxProduct([2,3,-2,4]))