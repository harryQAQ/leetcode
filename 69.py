class Solution:
    def mySqrt(self, x: int) -> int:
        if x >= 4:
            l, r = 0, x // 2
        else:
            l, r = 0, x
        while l < r:
            mid = (l + r + 1) >> 1  #条件一定要取右中位数
            if mid * mid > x: #满足改条件一定不是解
                r = mid - 1
            else:
                l = mid
        return l
            

x = Solution()
print(x.mySqrt(8))