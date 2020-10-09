### 递归算法
from utils import *
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        return [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)


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
                stack.append((0, node.right))
                stack.append((0, node.left))
                stack.append((1, node))
            else:
                ret.append(node.val)
        return ret

class Solution2:
    def inorderTraversal(self, root: TreeNode):
        ret = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ret


root = create_tree([1, 2, 3, 4, 5, 6, 7, 8])
ret1 = Solution().inorderTraversal(root)
ret2 = Solution1().inorderTraversal(root)
ret3 = Solution2().inorderTraversal(root)

print(ret1)
print(ret2)
print(ret3)