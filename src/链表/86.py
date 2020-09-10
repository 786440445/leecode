'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = ListNode(None)
        root = less_head
        more_head = ListNode(None)
        tail = more_head
        while head is not None:
            if head.val < x:
                tmp = head.next
                head.next = None
                less_head.next = head
                less_head = less_head.next
                head = tmp
            else:
                tmp = head.next
                head.next = None
                more_head.next = head
                more_head = more_head.next
                head = tmp
        less_head.next = tail.next
        return root.next


from utils import *
head = create_list_node([1, 3, 4, 2, 2, 5, 6])
print_list(Solution().partition(head, 4))
