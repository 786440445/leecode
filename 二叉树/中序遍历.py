from utils import *
# 递归算法
class Solution1:
    def midbianli(self, root):
        if root is None:
            return []
        return self.midbianli(root.left) + [root.val] + self.midbianli(root.right)


class Solution3:
    def midbianli(self, root):
        ret = []
        stack = []
        stack.append((0, root))
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == 0:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
            else:
                ret.append(node.val)
        return ret


class Solution2:
    def midbianli(self, root):
        ret = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret


root = create_tree([1, 2, 3, 4, 5, 6, 7, 8])
ret1 = Solution1().midbianli(root)
ret2 = Solution2().midbianli(root)
ret3 = Solution3().midbianli(root)

print(ret1)
print(ret2)
print(ret3)
