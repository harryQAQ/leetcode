from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                tmpNode = queue.pop(0)
                if tmpNode.left:
                    queue.append(tmpNode.left)
                if tmpNode.right:
                    queue.append(tmpNode.right)
                if i == size - 1:
                    res.append(tmpNode.val)
        return res