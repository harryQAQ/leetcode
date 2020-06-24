# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def dfs(L: TreeNode, R: TreeNode):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False 
            return dfs(L.right, R.left) and dfs(L.left, R.right)

        if not root: return True
        return dfs(root.left, root.right)