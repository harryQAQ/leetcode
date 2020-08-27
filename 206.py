class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        pre, cur = None, head
        tmp = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre