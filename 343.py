from functools import lru_cache

class Solution:
    # 自顶向下，记忆化搜索
    # @lru_cache
    # def integerBreak(self, n: int) -> int:
    #     if n == 2: return 1
    #     res = 0
    #     for i in range(1, n):
    #         res = max(res, max(i * self.integerBreak(n - i), i * (n - i)))
    #     return res

    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        # i 表示现在计算哪一轮值
        for i in range(3, n + 1):
            # j  1 ~ n - 1      j * dp[i - j] 和 j * (i - j )
            # 到一半就可以
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(dp[i - j] * j, (i - j) * j))
        return dp[n]