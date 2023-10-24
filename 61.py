# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        tail = head
        llen = 0
        if tail is None or tail.next is None:
            return head

        while tail.next is not None:
            tail = tail.next
            llen += 1

        llen += 1


        k = k % llen

        if k == 0:
            return head
        index = llen - k
        preone = llen - k - 1

        pre1 = head
        i = 0
        while i < preone:
            pre1 = pre1.next
            i += 1

        nextone = pre1.next
        pre1.next = None
        tail.next = head

        return nextone



        #从倒数第k个截断，安装在原链表的前面，倒数第k个的索引是llen-k
