# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        l = list()
        p = head
        while p is not None:
            l.append(p)
            p = p.next
        # print(l)
        pre = None
        while len(l) != 0:
            p = l.pop(0)
            if pre is not None:
                pre.next = p

            if len(l) == 0:
                p.next = None
                break
            q = l.pop(-1)
            p.next = q
            pre = q
            if len(l) == 0:
                pre.next = None
                break

        return head