from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i // 2):
                dp[i] += 2 * dp[j] * dp[i - j - 1]
            if i & 1:
                dp[i] += dp[i // 2] ** 2
        return dp[-1]

x = Solution()
print(x.numTrees(5))
