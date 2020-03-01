from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        K = 1 #当前交易次数
        n = len(prices)
        if K >= n // 2:
            return self.greedy(prices)

        MP = [[[0] * 2 for _ in range(K + 1)] for _ in range(len(prices))]
        res = []
        # 设置初始状态,也就是第1天(i = 0),当k = 0时表示第1天不持股的状态一定是0收益，k = 1表示持股，-price[0]
        for i in range(K+1):
            MP[0][i][0], MP[0][i][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            for k in range(K + 1):
                # if not k:#k = 0，一定不持有股票
                #     MP[i][k][0] = MP[i]
                if not k:
                    MP[i][k][0] = MP[i - 1][k][0]
                else:
                    MP[i][k][0] = max(MP[i - 1][k][0], MP[i - 1][k - 1][1] + prices[i])
                MP[i][k][1] = max(MP[i - 1][k][1], MP[i - 1][k][0] - prices[i])
        for k in range(K + 1):
            res.append(MP[n - 1][k][0])

        return max(res)
    

    def greedy(self, prices):
        res, n = 0, len(prices)
        for i in range(1, n):
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]
        return res

    

