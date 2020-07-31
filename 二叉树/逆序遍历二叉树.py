from queue import Queue
from collections import deque
class Solution:
    def inverseTree(self, root):
        if root is None: return []
        ret = []
        de = deque()
        level = 1
        de.append((root, level))
        while de:
            tmp = deque()
            for _ in range(len(de)):
                (node, level) = de.popleft()
                if level % 2 == 0:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    de.append((node.left, level + 1))
                if node.right:
                    de.append((node.right, level + 1))
            ret.append(list(tmp))
        return ret


from utils import create_tree
cli = Solution()
print(cli.inverseTree(create_tree([1,2,3,4,5,6,7,8,9])))

###思路：
# 使用队列将节点按照正常层次遍历顺序存储
# 使用双端队列将节点的值进行存储。奇数层的节点从右边插入，偶数层的节点从左边插入。