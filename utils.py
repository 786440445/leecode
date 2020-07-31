
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list_node(l):
    head = ListNode(0)
    p = head
    for i in l:
        q = ListNode(i)
        p.next = q
        p = q
    return head.next


def print_list(head):
    ret = []
    while head!= None:
        ret.append(head.val)
        head = head.next
    print(ret)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 完全二叉树的层次遍历，构造树结构
from queue import Queue

def create_tree(list1):
    queue = Queue()
    root = TreeNode(list1[0])
    queue.put(root)
    for index in range(len(list1))[1::2]:
        head = queue.get()
        left = TreeNode(list1[index])
        head.left = left
        queue.put(left)
        if index+1 < len(list1):
            right = TreeNode(list1[index+1])
            head.right = right
            queue.put(right)
    return root


# 层次遍历打印二叉树
def print_tree(root):
    de = Queue()
    de.put(root)
    ret = []
    while not de.empty():
        node = de.get()
        ret.append(node.val)
        if node.left:
            de.put(node.left)
        if node.right:
            de.put(node.right)
    print(ret)