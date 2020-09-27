'''
637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。



示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from queue import Queue

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = Queue()
        q.put(root)
        ret = []
        while not q.empty():
            sum = 0
            l = q.qsize()
            for _ in range(l):
                root = q.get()
                sum += root.val
                if root.left:
                    q.put(root.left)
                if root.right:
                    q.put(root.right)
            ret.append(sum / l)

        return ret


print([a**a for a in range(3)])