from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board: return []
        if not words: return []

        self.res = set()
        self.m, self.n = len(board), len(board[0])
        #创建字典树
        root = TrieNode()
        #visit数组
        vis = [[False for _ in range(self.n)] for _ in range(self.m)]
        #将所有的待查找词都放进去
        for word in words:
            tmp = root
            for c in word:
                tmp = tmp.child[c]
            tmp.is_word = True
        
        def _dfs(x, y, now_word, now_dic):
            now_word += board[x][y]
            now_dic = now_dic.child[board[x][y]]
            #递归边界，递归到字典树的叶子结点
            if now_dic.is_word:
                #!!!!!!!!
                #这里如果return结果就不全，因为可能有部分的单词前缀包含在其他的单词里！
                #!!!!!!!!
                now_dic.is_word = False
                self.res.add(now_word)

            vis[x][y] = True
            
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + i, y + j
                if 0 <= next_x < self.m and 0 <= next_y < self.n and board[next_x][next_y] in now_dic.child and not vis[next_x][next_y]:
                    _dfs(next_x, next_y, now_word, now_dic)
            vis[x][y] = False
        

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root.child:
                    _dfs(i, j, '', root)
        return list(self.res)


x = Solution()

print(x.findWords([
  ['a', 'a']
],
['aaa']))