from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
        self.rank = [1 for _ in range(n)]

    def get_cnt(self):
        return self.count

    def find(self, x):
        if self.parent[x] == x:
            return x
        boss = self.find(self.parent[x])
        self.parent[x] = boss
        return boss

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1
        self.count -= 1

    def is_connected(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for it in equations:
            if it[1] == '=':
                uf.union(ord(it[0]) - 97, ord(it[3]) - 97)
        for it in equations:
            if it[1] == '!' and uf.is_connected(ord(it[0]) - 97, ord(it[3]) - 97):
                return False
        return True


x = Solution()
print(x.equationsPossible(["c==c","b==d","x!=z"]))