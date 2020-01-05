from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        #映射关系
        mp = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        def dfs(tmpstr, idx):
            if idx == len(digits): #递归边界
                res.append(tmpstr)
                return
            tmpNum = digits[idx]
            nowletters = mp[ord(tmpNum) - ord('0')]
            for letter in nowletters:
                dfs(tmpstr + letter, idx + 1)

        dfs('', 0)
        return res



x = Solution()
print(x.letterCombinations('23'))