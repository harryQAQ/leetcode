from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int: #[7,1,5,3,6,4]
        if not prices: return 0
        res = 0
        for i, _ in enumerate(prices):
            if i >= 1 and prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res