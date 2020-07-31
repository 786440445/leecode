'''
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        ret = ListNode(0)
        ret.next = head
        second = ret
        for i in range(n):
            second = second.next
        first = ret
        while(second.next != None):
            first = first.next
            second = second.next
        first.next = first.next.next
        return ret.next


def create_list_node(l):
    head = ListNode(0)
    p = head
    for i in l:
        q = ListNode(i)
        p.next = q
        p = q
    return head.next


def print_list(head):
    while head!= None:
        print(head.val)
        head = head.next


l1 = create_list_node([1, 2, 3])
cli = Solution()
ret = cli.removeNthFromEnd(l1, 3)
print_list(ret)
