class Solution:
    def validPalindrome(self, s: str) -> bool:
        judge = lambda s: s == s[::-1]
        #
        #o(n^2)超时
        # if len(s) <= 0: return True
        # tmp_str = s
        # if judge(tmp_str):
        #         return True
        # for i in range(len(s)):
        #     tmp_str = s[:i] + s[i + 1:]
        #     if judge(tmp_str):
        #         return True
        # return False
        if len(s) <= 1: return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return judge(s[left, right]) or judge(s[left + 1, right + 1])
        return True





x = Solution()
print(x.validPalindrome("abca"))