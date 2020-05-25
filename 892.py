from typing import List
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n, res = len(grid), 0
        for i in range(n):
            #>0即满足这个公式
            res += sum([4 * n + 2 if n > 0 else 0 for n in grid[i]])
            #减去所有当前行的重叠
            res -= 2 * sum([min(grid[i][j], grid[i][j - 1]) for j in range(1, n)])
            #减去与上一行的重叠
            if i > 0:
                res -= 2 * sum([min(grid[i - 1][j], grid[i][j]) for j in range(n)])
        return res


