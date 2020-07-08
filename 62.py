class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(dp)
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # return dp[-1][-1]
        pre, cur = [1] * n, [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j - 1] + pre[j]
            pre = cur[:]
        return cur[-1]

x = Solution()
print(x.uniquePaths(3, 2))