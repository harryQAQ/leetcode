# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [[root, 0, 1]]
        res = -1
        while queue:
            this_layer_pos = []
            for i in range(len(queue)):
                tmp_node, tmp_layer, tmp_pos = queue.pop(0)
                this_layer_pos.append(tmp_pos)
                if tmp_node.left:
                    queue.append([tmp_node.left, tmp_layer + 1, 2 * tmp_pos])
                if tmp_node.right:
                    queue.append([tmp_node.right, tmp_layer + 1, 2 * tmp_pos + 1])
            if this_layer_pos[-1] - this_layer_pos[0] + 1 > res:
                res = this_layer_pos[-1] - this_layer_pos[0] + 1
        return res