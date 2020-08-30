class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def maxDepth(root):
            global res
            if not root:
                return 0
            leftHeight = maxDepth(root.left)
            rightHeight = maxDepth(root.right)
            res = max(res, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        maxDepth(root)