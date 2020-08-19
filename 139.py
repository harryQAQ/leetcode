from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True 
        return dp[-1]


# from functools import lru_cache

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         @lru_cache(None)
#         def back_track(s):
#             if(not s):
#                 return True
#             res=False
#             for i in range(1,len(s)+1):
#                 if(s[:i] in wordDict):
#                     res=back_track(s[i:]) or res
#             return res
#         return back_track(s)
