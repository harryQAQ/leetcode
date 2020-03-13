from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        res = ListNode(-1)
        p = res
        while p1 and p2:
            if p1.val <= p2.val:
                tmp = ListNode(p1.val)
                p.next = tmp
                p1 = p1.next
            else:
                tmp = ListNode(p2.val)
                p.next = tmp
                p2 = p2.next
            p = p.next
        while p1:
            tmp = ListNode(p1.val)
            p.next = tmp
            p1 = p1.next
            p = p.next
        while p2:
            tmp = ListNode(p2.val)
            p.next = tmp
            p2 = p2.next
            p = p.next
        return res.next