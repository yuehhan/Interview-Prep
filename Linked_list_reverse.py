# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        prev = dummy = ListNode(0)
        dummy.next = head
        
        for i in range(m):
            cur = cur.next
            prev = prev.next
        
        for j in range(n-m):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        prev.next.next = nxt
        return dummy
    