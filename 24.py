# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        tail = ListNode()
        tail.next = head
        pre1 = tail

        while tail is not None and tail.next is not None:
            tail.next = self.remain(tail.next)
            tail = tail.next.next

        return pre1.next

    def remain(self,remaining):
        if remaining is None or remaining.next is None:
            return remaining
        else:
            temp = remaining
            pre1 = remaining.next.next
            remaining = remaining.next
            remaining.next = temp
            temp.next = pre1

            return remaining





