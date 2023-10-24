# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """


        if head is None or head.next is None:
            return head

        confirmed = ListNode()
        head1 = confirmed
        confirmed.next = head

        i = 0

        while i < left - 1:
            i += 1
            confirmed = confirmed.next

        p = confirmed.next.next
        pre1 = confirmed.next
        i += 1
        while i < right:
            pre = confirmed.next

            tail = p.next

            confirmed.next = p
            p.next = pre
            pre1.next = tail


            p = tail
            i += 1

        return head1.next




