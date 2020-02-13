from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, numLeft, numRight):
            if numLeft > n or numRight > n or numRight > numLeft:
                return
            if numLeft == n and numRight == n:
                res.append(s)
            dfs(s + '(', numLeft + 1, numRight)
            dfs(s + ')', numLeft, numRight + 1)
        dfs('', 0, 0)
        return res


x = Solution()
print(x.generateParenthesis(3))