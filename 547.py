from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
        self.rank = [1 for _ in range(n)]

    def get_count(self):
        return self.count
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        boss = self.find(self.parent[x])
        self.parent[x] = boss
        return boss
    
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if q_root == p_root:
            return
        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1
        #只要进行union操作，count--
        self.count -= 1

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        n = len(M)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == '1':
                    uf.union(i, j)
        return uf.count

x = Solution()
print(x.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))