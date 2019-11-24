# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        Nhead = ListNode(-1) 
        Nhead.next = head
        pre = Nhead
        while pre.next and pre.next.next:
            first, second = pre.next, pre.next.next
            pre.next = second
            first.next = second.next
            second.next = first
            pre = pre.next.next
        return Nhead.next
            
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

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    head = createList(a)
    x = Solution()
    b = x.swapPairs(head)
    printList(b)
