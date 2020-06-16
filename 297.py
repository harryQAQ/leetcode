from collections import deque
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root : TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        q = deque()
        q.extend([root])
        res = []
        while(q):
            node = q.popleft()
            res.append(str(node.val) if node else '#')
            if node: q.extend([node.left, node.right])
        return ','.join(res)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return

        nodes = [(TreeNode(int(v)) if v != '#' else None) for v in data.split(',')]
        i, j = 0, 1
        while j < len(nodes):
            if nodes[i] is not None:
                nodes[i].left = nodes[j]
                j += 1
                nodes[i].right = nodes[j]
                j += 1
            i += 1
        return nodes[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))