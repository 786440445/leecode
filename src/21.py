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