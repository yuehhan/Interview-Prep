class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None    
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        tmp = ListNode(val)
        if not self.head:
            self.head,self.tail = tmp,tmp
        else:
            tmp.next = self.head
            self.head = tmp
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        tmp = ListNode(val)
        if not self.head:
            self.head,self.tail = tmp,tmp
        else:
            self.tail.next = tmp
            self.tail = tmp
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return -1
        elif index == 0 or index == -1:
            self.addAtHead(val)
        else:
            tmp = ListNode(val)
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            tmp.next = cur.next
            cur.next = tmp
            if tmp.next is None:
                self.tail = tmp
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        cur = self.head
        if index >= self.size or not self.head or index < 0:
            return -1
        elif index == 0:
            self.head = cur.next
            if not self.head:
                self.tail = None
        else:
            cur = self.head
            for _ in range(index-1):
                if cur.next is None:
                    return
                cur = cur.next
            cur.next = cur.next.next
            if cur.next is None:
                self.tail = cur
        self.size -= 1