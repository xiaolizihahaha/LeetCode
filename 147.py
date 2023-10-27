# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):

        head1 = ListNode()

        while head is not None:
            current = head
            head = head.next
            current.next = None

            p = head1
            while p.next is not None:
                if p.next.val > current.val:
                    break
                p = p.next

            pnext = p.next
            p.next = current
            current.next = pnext

        return head1.next

