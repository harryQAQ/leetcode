class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        elif n == 2: return max(nums)
        res = 0
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            if dp[i] > res:
                res = dp[i]

        return res