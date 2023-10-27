# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 1
        head1 = ListNode()
        head2 = ListNode()
        head2.next = head
        head1.next = None

        p = head2
        q = head1

        if head is None or head.next is None:
            return head

        while p.next is not None:
            if i % 2 == 1:
                p = p.next
            if i % 2 == 0:
                pnext = p.next
                qnext = q.next

                p.next = pnext.next
                pnext.next = None
                q.next = pnext
                q = q.next

            i += 1

        p.next = head1.next
        return head



