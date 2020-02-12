from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# #BFS
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root : return []
#         q = collections.deque()
#         res = []
#         q.append(root)
#         count = 0
#         while q:
#             now_len = q.__len__()
#             res.append([])
#             for _ in range(now_len):
#                 tmp_node = q.popleft()
#                 res[count].append(tmp_node.val)
#                 if tmp_node.left : q.append(tmp_node.left)
#                 if tmp_node.right : q.append(tmp_node.right)
#             count += 1
#         return res


#DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(level, root):
            if not root: return
            if len(res) == level: res.append([]) #注意判断条件，level从0开始
            res[level].append(root.val)
            dfs(level + 1, root.left)
            dfs(level + 1, root.right)
        dfs(0, root)
        return res