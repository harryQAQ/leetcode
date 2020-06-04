class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [None] * (K + W)
        tmp = 0
        for i in range(K, len(dp)):
            dp[i] = 1 if i <= N else 0
            tmp += dp[i]
        
        for i in range(K - 1, -1, -1):
            dp[i] = tmp / W
            tmp = tmp + dp[i] - dp[i + W]
        return dp[0]




x = Solution()
print(x.new21Game(10, 1, 10))

