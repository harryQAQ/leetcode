# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res = float('-inf')
        def dfs(height, root):
            nonlocal res
            #若不加这句，运行会出错，因为对于maxDepth，res是局部变量，对于dfs，res是非全局的外部变量
            #当dfs修改res时，会自动将res转化为dfs的局部变量，屏蔽掉上层函数中的定义，若仅仅读取是不会出错的
            #使用了nonlocal res后，在dfs()中就不再将res视为dfs的内部变量，上层函数中对x的定义就不会被屏蔽掉。
            if not root: return
            if height > res:
                res = height
            dfs(height + 1, root.left)
            dfs(height + 1, root.right)
        dfs(1, root)
        return res