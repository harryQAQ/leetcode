class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # s = str(x)
        # flag = True
        # for i in range(len(s) // 2):
        #     if(s[i] != s[len(s) - i - 1]):
        #         flag = False
        #         break
        # return flag
        s1 = str(x)
        s2 = s1[::-1]
        return True if s1 == s2 else False



x = Solution()
print(x.isPalindrome(1001))