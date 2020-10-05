'''
117. 填充每个节点的下一个右侧节点指针 II
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from queue import Queue

class Solution:
    def connect(self, root):
        if not root:
            return root
        q = Queue()
        q.put(root)
        while not q.empty():
            layer = []
            size = q.qsize()
            lastNode = None
            while size > 0:
                node = q.get()
                if not lastNode:
                    lastNode = node
                else:
                    lastNode.next = node
                    lastNode = node
                layer.append(node)
                size -= 1
            if lastNode:
                lastNode.next = None
            for node in layer:
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return root




