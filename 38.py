class Solution:
    def countAndSay(self, n: int) -> str:
        pre = '1'
        for i in range(1, n):
            nxt, num, cnt = '', pre[0], 1
            for j in range(1, len(pre)):
                if pre[j] == num:
                    cnt += 1
                else:
                    nxt += str(cnt) + num
                    num, cnt = pre[j], 1
            nxt += str(cnt) + num
            pre = nxt
        return pre
            
x = Solution()

print(x.countAndSay(3))
