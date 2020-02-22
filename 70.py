class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 2
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    

x = Solution()
print(x.climbStairs(2))