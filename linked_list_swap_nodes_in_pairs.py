# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        dummy = pre = ListNode(0)
        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = cur
            pre.next = nxt
            cur = cur.next
            pre = nxt.next
        return dummy.next
            