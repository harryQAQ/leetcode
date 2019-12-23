class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        if slen <= 1:
            return s
        maxlen, res = 1, s[0]
        dp = [[False] * slen for _ in range(slen)]
        for r in range(1, slen):
            for l in range(r):
                #状态转移方程
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if r - l + 1 > maxlen:
                        maxlen, res = r - l + 1, s[l: r + 1]
        return res


x = Solution()
print(x.longestPalindrome("ac"))