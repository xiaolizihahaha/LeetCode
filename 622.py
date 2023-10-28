class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = self.head

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size >= self.capacity:
            return False
        else:

            if self.isEmpty():
                self.head = ListNode(value)
                self.tail = self.head
            else:
                newnode = ListNode(value)
                self.tail.next = newnode
                self.tail = self.tail.next

            self.size += 1
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.size <= 0:
            return False
        else:
            self.head = self.head.next

            self.size -= 1
            return True


    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.head.val


    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1

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
        if self.size == self.capacity:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()