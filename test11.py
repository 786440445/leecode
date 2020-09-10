# class TreeNode:
#     def __init__(self, value):
#         self.val=value
#         self.left = None
#         self.right = None
#
#
# from collections import deque
# class Solution():
#     def deal(self, root):
#         ret = []
#         de = deque()
#         de.append(root)
#         while de:
#             layer = []
#             for _ in range(len(de)):
#                 node = de.popleft()
#                 layer.append(node.val)
#                 if node.left:
#                     de.append(node.left)
#                 if node.right:
#                     de.append(node.right)
#             ret.append(layer)
#         return ret
#
#
# a = [1, 2, 3, 4, 5, 6]
# head = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
#
# head.left = node2
# head.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
#
# cli = Solution()
# ret = cli.deal(head)
#
#
# print(ret)


class w:
    def __init__(self, name):
        self.name = name
        self.__age=15

    def __sect(self):
        print('年齡是%d'% self.__age)
a = w('aaa')
# print(a.age)
print(a.name)

# a.__s