# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        q = []
        if not root: return 0
        q.append((1, root))
        flag, res = False, 0
        while q:
            now_qlen = len(q)
            for _ in range(now_qlen):
                tmp_node = q.pop(0)
                if tmp_node[1].left:
                    q.append((tmp_node[0] + 1, tmp_node[1].left))
                if tmp_node[1].right:
                    q.append((tmp_node[0] + 1, tmp_node[1].right))
                if not tmp_node[1].left and not tmp_node[1].right:
                    res, flag = tmp_node[0], True
                    break
            if flag: break
        return res
                    
