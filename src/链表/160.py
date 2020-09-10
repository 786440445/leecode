'''
160. 相交链表
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：



在节点 c1 开始相交。



示例 1：


'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        if a is None or b is None:
            return None
        while a is not None and b is not None:
            if a == b:
                return a
            a = a.next
            b = b.next
        if a is None:
            a = headB
        if b is None:
            b = headA
        while a is not None or b is not None:
            if a is None:
                a = headB
            if b is None:
                b = headA
            if a == b:
                return a
            a = a.next
            b = b.next
        return None
