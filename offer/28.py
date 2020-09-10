'''
剑指 Offer 28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3



示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
'''
from utils import *

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def judge(node1, node2):
            if node1 == None and node2 == None:
                return True
            elif node1 != None and node2 != None:
                return judge(node1.left, node2.right) and judge(node2.left, node1.right) and node1.val == node2.val
            return False
        return judge(root, root)
