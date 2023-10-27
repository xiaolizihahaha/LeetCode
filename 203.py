# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head1 = ListNode()
        head1.next = head

        pre = head1
        p = pre.next
        while p is not None:

            if p.val == val:
                pre.next = p.next

                p = pre.next
            else:
                pre = pre.next
                p = pre.next

        return head1.next