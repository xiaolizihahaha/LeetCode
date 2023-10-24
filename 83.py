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
        p = head
        confirmed = head
        if p is None:
            return head

        while p is not None and p.next is not None:
            if p.val != p.next.val:
                confirmed.next = p.next
                confirmed = confirmed.next
                p = p.next
            else :
                p = p.next
        confirmed.next = None

        return head
