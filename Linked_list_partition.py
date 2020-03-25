# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller = small = ListNode(0)
        bigger = big = ListNode(0)
        
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                bigger.next = head
                bigger = bigger.next
            head = head.next
        
                
        bigger.next = None
        smaller.next = big.next
        return small.next