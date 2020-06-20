#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 707
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/6 7:08 PM
@Desc   ：
=================================================='''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        p = self.head.next
        while p != None:
            index -= 1
            if index == 0:
                return p.val
            else:
                p = p.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        p = ListNode(val)
        p.next = self.head.next
        self.head.next = p

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail = ListNode(val)
        p = self.head
        while (p.next == None):
            p = p.next
        p.next = tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        p = self.head
        while (--index != 0):
            if p.next == None:
                node = ListNode(val)
                node.next = p.next
                p.next = node
            else:
                p = p.next

        node = ListNode(val)
        node.next = p.next
        p.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        p = self.head
        while (--index):
            if p.next == None:
                pass
            else:
                p = p.next
        p = p.next.next

# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    linkedList = MyLinkedList()
    print(linkedList)
    linkedList.addAtHead(1)
    print(linkedList)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    linkedList.get(1)
    linkedList.deleteAtIndex(1)
    linkedList.get(1)