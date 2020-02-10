# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        if q.val < root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if q.val > root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)