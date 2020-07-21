class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        def build_tree(left, right):
            res = []
            if left > right:
                return [None]
            for i in range(left, right + 1):
                left_trees = build_tree(left, i - 1)
                right_trees = build_tree(i + 1, right)
                for l in left_trees:
                    for r in right_trees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        res.append(curr_tree)
            return res
        
        return build_tree(1, n)

