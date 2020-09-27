'''
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

from queue import Queue
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ret = []
        while q:
            tmp = []
            path = []
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                tmp.append(node)
                path.append(node.val)
            ret.append(path[-1])
            for node in tmp:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ret


from utils import create_tree
root = create_tree([1,2,3,4,5,6])
ret = Solution().rightSideView(root)
print(ret)