# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode()
        large = ListNode()
        large1 = large
        small1 = small

        p = head

        while p is not None:
            if p.val < x:
                small.next = p
                small = small.next
            else:
                large.next = p
                large = large.next

            p = p.next

        small.next = None
        large.next = None

        small.next = large1.next

        return small1.next
