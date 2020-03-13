from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # n个小朋友
        n = num_people
        # 套用推出来的公式，直接计算可以完整发放糖果的次数p
        p = int((2 * candies + 0.25)**0.5 - 0.5) 
        # 算出完整发放糖果以后剩余的糖果数量
        R = int(candies - (p + 1) * p * 0.5)

        # 迭代rows轮，cols是倒霉孩子的下标
        rows, cols = p // n, p % n

        res = [0] * n
        for i in range(n):
            res[i] = (i + 1) * rows + int(rows * (rows - 1) * 0.5) * n

            # 最后一轮or在p<n时的第一轮
            if i < cols:
                res[i] += i + 1 + rows * n
        #最后一个小孩拿
        res[cols] += R
        return res

x = Solution()
print(x.distributeCandies(7, 4))