class ListNode(object):
    def __init__(self,key = '', val = 0, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):

    def __init__(self):
        self.head = None

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.head is None:
            newnode = ListNode()
            newnode.val = value
            newnode.key = key
            newnode.next = None
            self.head = newnode

        else:
            if self.get(key) == -1:
                newnode = ListNode()
                newnode.val = value
                newnode.key = key
                newnode.next = None
                newnode.next = self.head
                self.head = newnode
            else:
                p = self.head
                while p is not None:
                    if p.key == key:
                        p.val = value
                        return
                    p = p.next

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        p = self.head
        if self.head is None:
            return -1
        else:
            while p is not None:
                if p.key == key:
                    return p.val
                p = p.next
            return -1


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        pre = self.head
        p = self.head
        if self.head is None:
            return
        else:
            if self.head.key == key:
                self.head = self.head.next
                return
            while p is not None and p.key != key:
                pre = p
                p = p.next

            if p is not None and p.key == key:
                pre.next = p.next
                return

            return

if __name__ == '__main__':

# Your MyHashMap object will be instantiated and called as such:
    obj = MyHashMap()
    obj.put(1,1)
    obj.put(2,2)
    obj.put(3, 3)
    # obj.put(2, 23)
    obj.remove(3)

    p = obj.head
    while p is not None:
        print(p.key,p.val)
        p = p.next


