<<<<<<< HEAD
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        cur = head
        stack = []
        
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                
                cur.child.prev = cur
                cur.next = cur.child
                cur.child = None
            
            if not cur.next and stack:
                node = stack.pop()
                
                node.prev = cur
                cur.next = node
            
            cur = cur.next
        
=======
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        cur = head
        stack = []
        
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                
                cur.child.prev = cur
                cur.next = cur.child
                cur.child = None
            
            if not cur.next and stack:
                node = stack.pop()
                
                node.prev = cur
                cur.next = node
            
            cur = cur.next
        
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return head