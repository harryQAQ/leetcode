from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        root_index = len(nums) // 2
        root = TreeNode(nums[root_index])

        left = nums[:root_index]
        right = nums[root_index + 1:]
        
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root