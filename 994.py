from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        count, res = 0, 0
        m, n = len(grid), len(grid[0])

        #list表示队列
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2: #所有坏橘子同时开始传播
                    queue.append([i, j])
        #还有好橘子，queue不空
        while count > 0 and queue:
            res += 1
            tmp_len = len(queue)
            for i in range(tmp_len):
                tmp_x, tmp_y = queue.pop(0)
                if tmp_x + 1 < m and grid[tmp_x + 1][tmp_y] == 1:
                    grid[tmp_x + 1][tmp_y] = 2
                    count -= 1
                    queue.append([tmp_x + 1, tmp_y])
                if tmp_x - 1 >= 0 and grid[tmp_x - 1][tmp_y] == 1:
                    grid[tmp_x - 1][tmp_y] = 2
                    count -= 1
                    queue.append([tmp_x - 1, tmp_y])
                if tmp_y + 1 < n and grid[tmp_x][tmp_y + 1] == 1:
                    grid[tmp_x][tmp_y + 1] = 2
                    count -= 1
                    queue.append([tmp_x, tmp_y + 1])
                if tmp_y - 1 >= 0 and grid[tmp_x][tmp_y - 1] == 1:
                    grid[tmp_x][tmp_y - 1] = 2
                    count -= 1
                    queue.append([tmp_x, tmp_y - 1])
        
        if count: return -1
        else: return res
x = Solution()
print(x.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
        
