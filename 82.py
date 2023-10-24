# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        confirmed = ListNode(val=-101)
        head1 = confirmed
        confirmed.next = head
        start = head
        p = head

        while p is not None:
            while start.val == p.val:
                p = p.next
                if p is None:
                    break
            if start.next == p:
                confirmed.next = start
                confirmed = confirmed.next
                start = start.next
            else:
                start = p

        confirmed.next = None




        return head1.next