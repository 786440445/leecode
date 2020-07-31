'''
剑指 Offer 07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。



例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


限制：

0 <= 节点个数 <= 5000

'''

from utils import *

### 递归算法,
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        ind = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:ind+1], inorder[:ind])
        root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        return root


class Solution1:
    def buildTree(self, preorder, inorder):

        pass

    def bps(self):

        pass


inorder = [8, 4, 2, 5, 1, 6, 3, 7]
preorder = [1, 2, 4, 8, 5, 3, 6, 7]

root = Solution().buildTree(preorder, inorder)

print_tree(root)