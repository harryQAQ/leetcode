from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k: return 0
        K = k #最大交易次数
        n = len(prices)
        #如果K很大，状态数组会非常大，内存会爆，其实当K大于序列一半时，就可以退化为无数次交易的情况了。
        if K >= n // 2:
            return self.greedy(prices)

        MP = [[[0] * 2 for _ in range(K + 1)] for _ in range(len(prices))]
        res = []
        #这里要假定买入股票算一次交易完成，那么在初始化的时候要对两个状态进行初始化
        # 设置初始状态
        MP[0][1][1] = -prices[0]
        for k in range(2, K+1):
            MP[0][k][1] = float('-inf')
        #由于假定 买入就算交易次数，任何一天，0次交易是不可能持股的
        for i in range(n):
            MP[i][0][1] = float('-inf')


        for i in range(1, len(prices)):
            for k in range(1, K + 1):
                MP[i][k][0] = max(MP[i - 1][k][0], MP[i - 1][k][1] + prices[i]) 
                MP[i][k][1] = max(MP[i - 1][k][1], MP[i - 1][k - 1][0] - prices[i]) #买入算一次交易
        for k in range(K + 1):
            res.append(MP[n - 1][k][0])

        return max(res)
    

    def greedy(self, prices):
        res, n = 0, len(prices)
        for i in range(1, n):
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]
        return res

    

