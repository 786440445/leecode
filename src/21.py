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