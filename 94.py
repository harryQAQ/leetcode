from typing import List 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root: return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res 
