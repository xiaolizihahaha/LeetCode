class ListNode(object):
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
class MyHashSet(object):

    def __init__(self):
        self.head = None

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        p = self.head
        pre = self.head
        newnode = ListNode(key)

        if self.head is None:
            self.head = newnode
        else:
            if key < self.head.val:
                newnode.next = self.head
                self.head = newnode
            elif key == self.head.val:
                return
            else:
                while p is not None and key > p.val:
                    pre = p
                    p = p.next

                if p is not None and key == p.val:
                    return

                prenext = pre.next
                pre.next = newnode
                newnode.next = prenext


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        p = self.head
        pre = self.head

        if self.head is None:
            return
        else:

            if key < self.head.val:
                return
            elif key == self.head.val:
                self.head = self.head.next
            else:
                while p is not None and key > p.val:
                    pre = p
                    p = p.next
                if p is None:
                    return
                if p.val == key:
                    pre.next = p.next
                return

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        p = self.head
        if self.head is None:
            return False
        else:
            while p is not None and p.val <= key:
                if p.val == key:
                    return True
                p = p.next
            return False



if __name__ == '__main__':


    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(3))
    obj.add(2)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.contains(2))

    p = obj.head
    while p is not None:
        print(p.val)
        p = p.next

