'''
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。



示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL


限制：

0 <= 节点个数 <= 5000

'''
from utils import *

class Solution:
    def reverseList(self, head):
        ret = ListNode(None)
        while head != None:
            p = head
            head = head.next
            end = ret.next
            ret.next = p
            ret.next.next = end
        return ret.next


cli = Solution()
ret = cli.reverseList(create_list_node([1, 2, 3, 4]))
print_list(ret)