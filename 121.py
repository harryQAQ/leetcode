from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        K = 1 #当前交易次数
        MP = [[[0] * 2 for _ in range(K + 1)] for _ in range(len(prices))]
        res = []
        # 设置初始状态, 无论什么k,第0天不持股一定是0收益，且不可能持股，可以处理成-price[0],或者-inf
        for i in range(K+1):
            MP[0][i][0], MP[0][i][1] = 0, -float('inf')

        for i in range(1, len(prices)):
            for k in range(K + 1):
                # if not k:#k = 0，一定不持有股票
                #     MP[i][k][0] = MP[i]
                if not k:
                    MP[i][k][0] = MP[i - 1][k][0]
                else:
                    MP[i][k][0] = max(MP[i - 1][k][0], MP[i - 1][k - 1][1] + prices[i])
                MP[i][k][1] = max(MP[i - 1][k][1], MP[i - 1][k][0] - prices[i])
                res.append(MP[i][k][0])
        return max(res)
                

