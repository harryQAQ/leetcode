from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        xy_diff = set()
        xy_add = set()
        res = []
        def dfs(row, tmp):
            if row >= n:
                if len(tmp) == n:
                    res.append(tmp)
                return None
            for col in range(n):
                if col in cols or row + col in xy_add or row - col in xy_diff:
                    continue
                cols.add(col)
                xy_diff.add(row - col)
                xy_add.add(row + col)
                dfs(row + 1, tmp + [col])
                cols.remove(col)
                xy_diff.remove(row - col)
                xy_add.remove(row + col)
        dfs(0, [])
        return [ ['.'* i + 'Q' + '.' * (n - i - 1)for i in tmp]for tmp in res]
                
x = Solution()
print(x.solveNQueens(4))
