'''
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        x = n - m + 1
        root = head
        pre_head = None
        while head is not None and m - 1 != 0:
            pre_head = head
            head = head.next
            m = m - 1
        modify_tail = head
        new_head = None
        while head and bool(x):
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            x -= 1

        modify_tail.next = head
        if pre_head is None:
            root = new_head
        else:
            pre_head.next = new_head
        return root

from utils import *
list1 = create_list_node([1, 2, 3, 4, 5, 6, 7])
print_list(Solution().reverseBetween(list1, 1, 5))
