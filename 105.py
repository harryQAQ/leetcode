# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preL: int, preR: int, inL: int, inR: int) -> TreeNode: 
            if preL > preR or inL > inR:
                return None
            root = TreeNode(preorder[preL])
            
            root_in_index = inL
            for i in range(inL, inR + 1):
                if inorder[i] == preorder[preL]:
                    root_in_index = i
                    break
            numLeft = root_in_index - inL
            # root.left = helper(preL + 1, preL + numLeft, preL + numLeft + 1, preR)
            # root.right = helper(inL, inL + numLeft - 1, root_in_index + 1, inR)
            root.left = helper(preL + 1, preL + numLeft,inL, inL + numLeft - 1)
            root.right = helper(preL + numLeft + 1, preR, root_in_index + 1, inR)
            return root 
            
        root = helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        return root


x = Solution()

print(x.buildTree([3,9,20,15,7], [9,3,15,20,7]))