def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l2: return l1
    if not l1: return l2
    if not l1 and l2: return None
    
    cur = dummy = ListNode(0)
    carry = 0
    
    while l1 or l2 or carry:
        if l1:
            carry+= l1.val
            l1 = l1.next
        if l2:
            carry+= l2.val
            l2 = l2.next
        
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry//= 10
    
    return dummy.next