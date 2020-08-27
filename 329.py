from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])

        lookup = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]
            
            res = 1
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nxt_x, nxt_y = x + i, y + j
                if 0 <= nxt_x < m and 0 <= nxt_y < n and \
                        matrix[nxt_x][nxt_y] > matrix[i][j]:
                    res = max(res, 1 + dfs(nxt_x, nxt_y))
                
            lookup[i][j] = max(res, lookup[i][j])
            return lookup[i][j]
        self.res = 0
        for i in range(m):
            for j in range(n):
                self.res = max(self.res, dfs(i, j))
        return self.res


