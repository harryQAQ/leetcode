# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #递归翻转链表的实现
    def reverseList(self, a: ListNode, b:ListNode) -> ListNode:
        pre = None
        first, second = a, b
        while first != b:
            second = first.next
            first.next = pre
            pre, first= first, second
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        a, b = head, head
        for i in range(k):
            if(b == None):
                return head
            b = b.next
        newHead = self.reverseList(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead

def printList(head: ListNode):
    p = head
    while p:
        print(p.val)
        p = p.next

def createList(a: list):
    Nhead = ListNode(-1)
    p = Nhead
    for i in a:
        tmp = ListNode(i)
        p.next = tmp
        p = p.next
    return Nhead.next

if __name__ == "__main__":
    head = createList([1, 2, 3, 4, 5])
    printList(head)
    x = Solution()
    test = x.reverseKGroup(head, 3)
    printList(test)