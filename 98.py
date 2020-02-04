# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cmp = []
        def helper(root: TreeNode):
            if not root: return
            helper(root.left)
            cmp.append(root.val)
            helper(root.right)
        helper(root)
        return sorted(cmp) == cmp and len(set(cmp)) == len(cmp) #第一遍写没有加上第二个判断条件，要保证没有重复的元素
