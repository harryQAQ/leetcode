class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.res = 0
        def dfs(queen, xy_diff, xy_sum):
            row = len(queen)  #当前序列长度表示递归到某一层
            if len(queen) == n:
                self.res += 1
                return
            for col in range(n):
                if col not in queen and row - col not in xy_diff and row + col not in xy_sum:
                    dfs(queen + [col], xy_diff + [row - col], xy_sum + [row + col])
        dfs([], [], [])
        return self.res