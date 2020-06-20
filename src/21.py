<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 21
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/6 11:55 PM
@Desc   ：
=================================================='''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        while(l1 != None and l2 != None):
            if l2.val > l1.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

        if l1 != None:
            head.next = l1
        if l2 != None:
            head.next = l2
        return head
=======
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create_list(self, list):
        s = ListNode(list[0])
        p = s
        for x in list[1:]:
            m = ListNode(x)
            p.next = m
            p = p.next
        return s

    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        cur = head
        while(l1 != None and l2 != None):
            if l1.val < l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if l1 == None:
            cur.next = l2
        if l2 == None:
            cur.next = l1
        return head.next


    def print(self, l1):
        while(l1 != None):
            print(l1.val)
            l1 = l1.next

solu = Solution()
l1 = solu.create_list([2])
l2 = solu.create_list([1])
l3 = solu.mergeTwoLists(l1, l2)
solu.print(l3)
>>>>>>> a7d9e50fc27dc8bc80e980ee215d92fe5da140f3
