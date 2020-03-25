<<<<<<< HEAD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # create 3 pointers
        #pointer 1 reaches the end of the list
        #pointer 2 is set to delay by n steps
        #final pointer skips over the node pointer 2 is at
        
        p1 = p2 = head
        dummy = p3 = ListNode(0)
        p3.next = p2
        
        for _ in range(n-1):
            p1 = p1.next
        
        while p1 and p1.next:
            p1 = p1.next
            p2 = p2.next
        
        while p3:
            if p3.next == p2:
                p3.next = p3.next.next
                p3 = p3.next
            else:
                p3 = p3.next
        
        return dummy.next
=======
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # create 3 pointers
        #pointer 1 reaches the end of the list
        #pointer 2 is set to delay by n steps
        #final pointer skips over the node pointer 2 is at
        
        p1 = p2 = head
        dummy = p3 = ListNode(0)
        p3.next = p2
        
        for _ in range(n-1):
            p1 = p1.next
        
        while p1 and p1.next:
            p1 = p1.next
            p2 = p2.next
        
        while p3:
            if p3.next == p2:
                p3.next = p3.next.next
                p3 = p3.next
            else:
                p3 = p3.next
        
        return dummy.next
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
