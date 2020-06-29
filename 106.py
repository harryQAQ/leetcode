from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.inorder, self.postorder = None, None

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        assert len(inorder) == len(postorder)
        n = len(inorder)
        self.inorder, self.postorder = inorder, postorder
        root = self.dfs(0, n - 1, 0, n - 1)
        return root

    def dfs(self, inL, inR, postL, postR):
        if inL > inR or postL > postR:
            return None
        
        root = TreeNode(self.postorder[postR])
        in_root_index = self.inorder.index(self.postorder[postR])
        numLeft = in_root_index - inL
        root.left = self.dfs(inL, inL + numLeft - 1, postL, postL + numLeft - 1)
        root.right = self.dfs(in_root_index + 1, inR, postL + numLeft, postR - 1)
        return root
        

        



