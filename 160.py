# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pre1 = headA
        pre2 = headB

        while pre1 is not None and pre2 is not None:
            pre1 = pre1.next
            pre2 = pre2.next

        if pre1 is None:
            pre1 = headB
            while pre2 is not None:
                pre2 = pre2.next
                pre1 = pre1.next
            if pre2 is None:
                pre2 = headA
                while pre1 != pre2:
                    pre1 = pre1.next
                    pre2 = pre2.next
        else:
            pre2 = headA
            while pre1 is not None:
                pre2 = pre2.next
                pre1 = pre1.next
            if pre1 is None:
                pre1 = headB
                while pre1 != pre2:
                    pre1 = pre1.next
                    pre2 = pre2.next
        return pre1





# if __name__ == '__main__':
#     solution = Solution()
#     solution.getIntersectionNode()
