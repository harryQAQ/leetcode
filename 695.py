from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        self.row, self.col = len(grid), len(grid[0])
        self.s = set()
        self.res, self.tmpcnt = 0, 0 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        def dfs(x, y, cnt):
            if not 0 <= x < self.row or not 0 <= y < self.col or grid[x][y] == 0:
                return
            self.tmpcnt += 1
            if self.tmpcnt > self.res:
                self.res = self.tmpcnt
            self.s.add((x, y))
            for dx, dy in directions:
                if (x + dx, y + dy) not in self.s:
                    dfs(x + dx, y + dy, cnt + 1)
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == 1 and (i, j) not in self.s:
                    self.tmpcnt = 0
                    dfs(i, j, 1)
        return self.res


x = Solution()
print(x.maxAreaOfIsland(([[1,1],[1,0]])))
            





