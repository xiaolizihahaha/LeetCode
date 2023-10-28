class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = self.head

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull() is True:
            return False
        else:
            if self.isEmpty() is True:
                newnode = ListNode(value)
                self.head = newnode
                self.tail = self.head
            else:
                newnode = ListNode(value)
                newnode.next = self.head
                self.head = newnode
            self.size += 1
            return True



    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull() is True:
            return False
        else:
            if self.isEmpty() is True:
                newnode = ListNode(value)
                self.head = newnode
                self.tail = self.head

            else:
                newnode = ListNode(value)
                self.tail.next = newnode
                self.tail = self.tail.next
            self.size += 1
            return True


    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty() is True:
            return False
        else:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                hnext = self.head.next
                self.head.next = None
                self.head = hnext
            self.size -= 1
            return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty() is True:
            return False
        else:
            if self.size == 1:
                self.head = None
                self.taio = None
            else:

                pre = self.head
                p = self.head

                while p.next is not None:
                    pre = p
                    p = p.next
                self.tail = pre
                self.tail.next = None
            self.size -= 1
            return True




    def getFront(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        else:
            return self.head.val


    def getRear(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        else:
            return self.tail.val


    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False


    def isFull(self):
        """
        :rtype: bool
        """
        if self.capacity == self.size:
            return True
        else:
            return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()