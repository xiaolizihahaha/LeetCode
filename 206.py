# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # p = head
        # head1 = ListNode()
        # while p is not None:
        #     newnode = ListNode(p.val)
        #     h1next = head1.next
        #     head1.next = newnode
        #     newnode.next = h1next
        # return head1.next

        #[1,2,3,4,5]
        #[5,4,3,2,1]

        p = head
        head1 = ListNode()

        while head is not None:
            p = head
            head = head.next
            p.next = None

            h1next = head1.next
            head1.next = p
            p.next = h1next

        return head1.next


