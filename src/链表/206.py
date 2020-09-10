'''
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head != None:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head


from utils import create_list_node
head = create_list_node([1,2,3,4,5])
Solution().reverseList(head)