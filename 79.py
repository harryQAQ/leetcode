from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        if not word: return True
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        m, n = len(board), len(board[0])
        self.flag = False
        def dfs(tmp_str, x, y):
            if tmp_str == word:
                self.flag = True
                return
            if len(tmp_str) > len(word):
                return
            if tmp_str[-1] != word[len(tmp_str) - 1]:
                return
            #设置已访问    
            tmp, board[x][y] = board[x][y], '!'
            for i in range(4):
                next_x, next_y = x + dx[i], y + dy[i]
                if 0 <= next_x < m and 0<= next_y < n and board[next_x][next_y] != '!' :
                    dfs(tmp_str + board[next_x][next_y], next_x, next_y)
                if self.flag: return
            board[x][y] = tmp
        for i1 in range(m):
            for j1 in range(n):
                if board[i1][j1] == word[0]:
                    dfs(word[0], i1, j1)
        return self.flag

x = Solution()

print(x.exist(
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCB"))