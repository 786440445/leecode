'''
501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ret = []
        ret.append((0, root))
        old_v = None
        count = 0
        res = 0
        while ret:
            color, node = ret.pop()
            if not node:
                continue
            if color == 0:
                ret.append((0, node.right))
                ret.append((1, node))
                ret.append((0, node.left))
            else:
                print(node.val)
                if count == 0:
                    res = node.val
                if not old_v or old_v == node.val:
                    count += 1
                    old_v = node.val
                else:
                    count -= 1
                    old_v = node.val
        return res


from utils import create_tree
root = create_tree([3, 2, 3, 1, 3, 3, 4])
ret = Solution().findMode(root)
print(ret)
