# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        
        
        dummy = ans = ListNode(0)
        for i in range(len(arr)):
            ans.next = ListNode(arr[i])
            ans = ans.next
        
        
        return dummy.next
            
    