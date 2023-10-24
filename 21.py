# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre1 = list1
        pre2 = list2
        list3 = ListNode()

        pre3 = list3

        while pre1 is not None and pre2 is not None:
            if pre1.val <= pre2.val:
                pre3.next = pre1
                pre3 = pre3.next
                pre1 = pre1.next
            else:
                pre3.next = pre2
                pre3 = pre3.next
                pre2 = pre2.next
        if pre1 is not None:
            pre3.next = pre1
        if pre2 is not None:
            pre3.next = pre2

        return list3.next