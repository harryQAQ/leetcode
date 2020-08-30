from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     def helper(root):
    #         if not root:
    #             return
    #         helper(root.right)
    #         helper(root.left)
    #         root.left, root.right = root.right, root.left
    #     helper(root)
    #     return root
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = [root]

        while queue:
            tmpNode = queue.pop(0)
            if tmpNode.left or tmpNode.right:
                tmpNode.left, tmpNode.right = tmpNode.right, tmpNode.left
            if tmpNode.left:
                queue.append(tmpNode.left)
            if tmpNode.right:
                queue.append(tmpNode.right)
        return root

