'''
404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
'''

from utils import TreeNode
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left and not node.left.left and not node.left.right:
                self.res += node.left.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return self.res