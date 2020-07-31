'''
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

### 递归算法
from utils import *
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


### 非递归算法，使用栈，增加一个颜色标记，对于中序，前序，后续都可以使用
from utils import *

class Solution1:
    def inorderTraversal(self, root: TreeNode):
        ret = []
        stack = []
        stack.append((0, root))
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == 0:
                stack.append((1, node))
                stack.append((0, node.right))
                stack.append((0, node.left))
            else:
                ret.append(node.val)
        return ret


class Solution2:
    def inorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res