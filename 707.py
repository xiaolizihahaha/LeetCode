class ListNode(object):
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = self.head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index > self.size -1:
            return -1
        if self.head is None:
            return -1

        i = 0
        p = self.head
        while i < index:
            i += 1
            p = p.next
        return p.val



    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            newnode = ListNode(val)
            self.head = newnode
            self.tail = newnode
        else:
            newnode = ListNode(val)
            newnode.next = self.head
            self.head = newnode

        self.size += 1


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            newnode = ListNode(val)
            self.head = newnode
            self.tail = newnode
        else:
            newnode = ListNode(val)
            self.tail.next = newnode
            self.tail = newnode
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        else:
            i = 0
            pre = self.head
            p = self.head
            while i < index:
                pre = p
                p = p.next
                i += 1
            newnode = ListNode(val)
            pre.next = newnode
            newnode.next = p


        self.size += 1


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index > self.size - 1:
            return

        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
        elif index == self.size - 1:
            p = self.head
            pre = self.head
            while p.next is not None:
                pre = p
                p = p.next
            self.tail = pre
            self.tail.next = None
        else:
            p = self.head
            pre = self.head
            i = 0
            while i < index:
                i += 1
                pre = p
                p = p.next
            pre.next = p.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:

if __name__ =='__main__':

    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtHead(2)

    obj.addAtHead(3)
    obj.addAtTail(4)
    obj.addAtIndex(5,6)
    obj.deleteAtIndex(3)


    p = obj.head
    while p is not None:
        print(p.val)
        p = p.next