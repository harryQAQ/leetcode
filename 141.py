# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        #定义一个set，然后不断遍历链表
        s = set()
        while head:
            #如果某个节点在set中，说明遍历到重复元素了，也就是有环
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False