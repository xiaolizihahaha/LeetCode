# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        head1 = ListNode()
        p = head
        while p is not None:
            h1next = head1.next
            newnode = ListNode(p.val)
            head1.next = newnode
            newnode.next = h1next

            p = p.next

        p = head
        q = head1.next

        while p is not None and q is not None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next

        return True
