from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        print(dp)


x = Solution()
print(x.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])) 
