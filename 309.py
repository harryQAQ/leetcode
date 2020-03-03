from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n <= 1: return 0
        MP = [[0] * 2 for _ in range(n + 1)]
        MP[1][1], MP[0][1] = -prices[0], float('-inf') #初始化
        prices.insert(0, 0)  # 下标1算第一天, 方便处理
        for i in range(2, n + 1):
            MP[i][0] = max(MP[i - 1][0], MP[i - 1][1] + prices[i])   #不动或卖掉
            MP[i][1] = max(MP[i - 1][1], MP[i - 2][0] - prices[i])   #不动或买入
        return MP[n][0]