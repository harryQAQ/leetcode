# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        mp = {-1: TreeNode(-1)}
        def addNode(height, node):
            mp[height] = node
            if not mp[height - 1].left:
                mp[height - 1].left = node
            else:
                mp[height - 1].right = node
        val, deep = '', 0
        for c in S:
            if c != '-':
                val += c
            elif val:
                addNode(deep, TreeNode(val))
                val, deep = '', 1
            else:
                deep += 1
        addNode(deep, TreeNode(val))
        return mp[0]

x = Solution()
print(x.recoverFromPreorder("1-2--3--4-5--6--7"))