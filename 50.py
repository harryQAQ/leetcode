# 递归
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         #一定要注意n < 0的情况 
#         def helper(x, n):
#             if not n: return 1
#             if n < 0: return 1 / helper(x, -n)
#             if n % 2: 
#                 return x * helper(x, n - 1)
#             return helper(x * x, n / 2)
#         return helper(x, n)  

#迭代
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0 :
            x, n = 1 / x, -n
        res, tmp = 1, x
        while n:
            if n & 1:
                res *= tmp
            tmp *= tmp
            n >>= 1
        return res


x = Solution()
print(x.myPow(2, 10))