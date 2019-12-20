# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        if not root: return
        yield from self.inorder(root.left)
        yield root.val
        yield from self.inorder(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        gen = self.inorder(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)   