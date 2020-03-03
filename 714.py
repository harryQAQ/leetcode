from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1: return 0
        prices.insert(0, 0)
        MP = [[0] * 2 for _ in range(n + 1)]
        MP[0][1] = float('-inf')
        for i in range(1, n + 1):
            MP[i][0] = max(MP[i - 1][0], MP[i - 1][1] + prices[i])
            MP[i][1] = max(MP[i - 1][1], MP[i - 1][0] - prices[i] -fee)
        return MP[n][0]