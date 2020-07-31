# # 双端队列
# from collections import deque
# # 队列
# from queue import Queue
# # 后进先出队列，类似栈
# from queue import LifoQueue
# # 优先级队列
# from queue import PriorityQueue

from utils import *

from queue import Queue
class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None: return []
        ret = []
        de = Queue()
        de.put(root)
        while not de.empty():
            node = de.get()
            ret.append(node.val)
            if node.left:
                de.put(node.left)
            if node.right:
                de.put(node.right)
        return ret


root = create_tree([1,2,3,4,5,6,7])
cli = Solution()
ret = cli.levelOrder(root)
print(ret)