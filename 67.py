class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # if not a: return b
        # if not b: return a

        # if len(a) >= len(b):
        #     rever_a = a[::-1]
        #     rever_b = b[::-1]
        # else:
        #     rever_a = b[::-1]
        #     rever_b = a[::-1]

        # rever_res = ''
        # cnt, carry= 0, 0

        # while cnt < len(rever_a):
        #     if cnt < len(rever_b):
        #         tmp = ord(rever_a[cnt]) - ord('0') + ord(rever_b[cnt]) - ord('0') + carry
        #     else:
        #         tmp = ord(rever_a[cnt]) - ord('0') + carry
        #     if tmp == 2:
        #         carry = 1
        #         tmp = 0
        #         rever_res += str(tmp) 
        #     elif tmp == 3:
        #         carry = 1
        #         tmp = 1
        #         rever_res += str(tmp) 
        #     else:
        #         carry = 0
        #         rever_res += str(tmp)
        #     cnt += 1
        # if carry:
        #     rever_res += '1'

        # return rever_res[::-1]

        rever_res = ''
        len_a, len_b = len(a), len(b)
        if len_a < len_b:
            a = '0' * (len_b - len_a) + a
        else:
            b = '0' * (len_a - len_b) + b
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            tmp = ord(a[i]) - ord('0') + ord(b[i]) - ord('0') + carry
            rever_res += str(tmp % 2)  #sum=2，这时候将sum%2=0放入结果集中
            carry = tmp // 2
        if carry:
            rever_res += '1'

        return rever_res[::-1]



x = Solution()
print(x.addBinary('111', '111'))
