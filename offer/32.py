"""
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
from utils import *
from collections import deque

from queue import Queue

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return []
        ret = []
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            layer = []
            for _ in range(queue.qsize()):
                node = queue.get()
                layer.append(node.val)
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            ret.append(layer)
        return ret
