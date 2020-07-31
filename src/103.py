'''
103. 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''

from utils import *
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None: return []
        ret = []
        de = deque()
        level = 1
        de.append((root, level))
        while de:
            tmp = deque()
            for _ in range(len(de)):
                (node, level) = de.popleft()
                if level % 2 == 0:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    de.append((node.left, level + 1))
                if node.right:
                    de.append((node.right, level + 1))
            ret.append(list(tmp))
        return ret

