'''
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic1 = dict()
        dic2 = dict()
        root = Node(0, None, None)
        p = root
        count = 1
        q = head
        while q:
            val = q.val
            next_ptr = q.next
            random_ptr = q.random
            dic1[q] = count
            cur = Node(val, None, None)
            dic2[count] = cur
            p.next = cur
            p = cur
            q = next_ptr
            count += 1

        # p = root.next
        q = head
        count = 1
        while q:
            cur = dic2[count]
            cur.random = dic2.get(dic1.get(q.random))
            q = q.next
            count += 1
        return root.next