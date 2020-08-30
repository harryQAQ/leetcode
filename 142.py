# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not (fast and fast.next):
                return
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return fast