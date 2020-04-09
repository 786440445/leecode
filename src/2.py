# Definition for singly-linked list.
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(list):
    head = ListNode(list[0])
    p = head
    for i, v in enumerate(list[1:]):
        node = ListNode(v)
        p.next = node
        p = node
    return head


def print_list(head):
    p = head
    while(p != None):
        print(p.val)
        p = p.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        re = ListNode(0)
        r = re
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            v = (carry + x + y) % 10
            carry = (carry + x + y) // 10
            p = ListNode(v)
            r.next = p
            r = p
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next

        if (carry > 0):
            r.next = ListNode(carry)
        return re.next


l1 = create_list([1])
l2 = create_list([9, 9])
head = Solution().addTwoNumbers(l1, l2)
print_list(head)