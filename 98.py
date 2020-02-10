# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#利用中序遍历判断 多写一个helper来进行inorder
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         cmp = []
#         def helper(root: TreeNode):
#             if not root: return
#             helper(root.left)
#             cmp.append(root.val)
#             helper(root.right)
#         helper(root)
#         return sorted(cmp) == cmp and len(set(cmp)) == len(cmp) #第一遍写没有加上第二个判断条件，要保证没有重复的元素


# #利用入口参数传递当前结点的最大最小值
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def isBST(root: TreeNode, min_val, max_val):
#             if not root:
#                 return True
#             if root.val >= max_val or root.val <= min_val:
#                 return False
#             return isBST(root.left, min_val, root.val) and isBST(root.right, root.val, max_val)
#         return isBST(root, float('-inf'), float('inf'))



#注意递归时每一个判断分支都要有return 最终也要有return
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None
        def helper(root: TreeNode):    
            if not root: return True
            if not helper(root.left):
                return False
            if self.pre and root.val <= self.pre.val:
                return False
            self.pre = root
            return helper(root.right)
        return helper(root)

