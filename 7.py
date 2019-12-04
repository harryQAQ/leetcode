class Solution:
    def reverse(self, x: int) -> int:
        #采用字符串翻转要单独处理溢出的问题
        of = (1<<31) - 1 if x > 0 else 1 << 31
        flag = 1
        if x < 0:
            flag = -1
            tmp = str(-x)
        else:    
            tmp = str(x)
        tmp = tmp[::-1]
        while len(tmp) > 0 and tmp[0] == '0':
            tmp = tmp[1:]
        tmp = '0' if len(tmp) == 0 else tmp
        if abs(int(tmp)) > of:
            return 0
        return flag * int(tmp)
        #直接翻转
        # y, res = abs(x), 0
        # of = (1 << 31) - 1 if x < 0 else 1 << 31
        # while y:
        #     res = res * 10 + y % 10
        #     if res > of:
        #         return 0
        #     y //= 10
        # return res if x > 0 else (-res)



x = Solution()
print(x.reverse(1534236469))         