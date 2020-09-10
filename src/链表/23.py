# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        size = len(lists)
        if size == 0:
            return None
        if size == 1:
            return lists[0]
        if size == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        mid = 2
        lis1 = lists[:size//mid]
        lis2 = lists[size//mid:]
        l1 = self.mergeKLists(lis1)
        l2 = self.mergeKLists(lis2)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        while(l1 != None and l2 != None):
            if l2.val > l1.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next

        if l1 != None:
            p.next = l1
        if l2 != None:
            p.next = l2
        return head.next


node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node7 = ListNode(2)
node8 = ListNode(6)
node1.next = node2.next
from utils import *
lists = [node1, [node4, node5, node6], [node7, node8]]
print_list(Solution().mergeKLists(lists))