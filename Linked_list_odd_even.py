# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        o = odds = ListNode(0)
        e = evens = ListNode(0)
        count = 1
        while head:
            if count%2:
                odds.next = head
                odds = head
            else:
                evens.next = head
                evens = head
                
            head = head.next
            count += 1
        
        odds.next = e.next
        evens.next = None
        return o.next