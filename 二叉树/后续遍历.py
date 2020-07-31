### 递归算法
from utils import *
class Solution1:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        return self.inorderTraversal(root.left) + self.inorderTraversal(root.right) + [root.val]


### 非递归算法，使用栈，增加一个颜色标记，对于中序，前序，后续都可以使用
from utils import *

class Solution2:
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

root = create_tree([1, 2, 3, 4, 5, 6, 7, 8])
ret1 = Solution1().inorderTraversal(root)
ret2 = Solution2().inorderTraversal(root)

print(ret1)
print(ret2)