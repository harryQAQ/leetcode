class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        dummy = ListNode(-1)
        dummy.next, slow, fast = head, dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        pre = None
        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        a, b = dummy.next, pre
        #注意这里是b，不是a
        while b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return True


a = ListNode(1)
b = ListNode(0)
c = ListNode(1)
a.next = b
b.next = c

x = Solution()
x.isPalindrome(a)