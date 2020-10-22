from utils import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        new_head = None
        while head != None:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head

head = create_list_node([1, 2, 3, 4, 5])
res = Solution().reverseList(head)
print_list(res)