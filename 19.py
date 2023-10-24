# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = head
        llen = 0

        while pre != None:
            pre = pre.next
            llen += 1

        index = llen - n

        pre = head
        i = 0

        if index < 1:
            return head.next

        while i < index - 1:
            pre = pre.next
            i += 1

        pre.next = pre.next.next
        return head




