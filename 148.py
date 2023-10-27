# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    #归并排序
    def sortList(self,head):

        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sortfunc(head):
            if head is None or head.next is None:
                return head
            slow = fast = pre = head
            while fast is not None and fast.next is not None:
                pre = slow
                slow = slow.next
                fast = fast.next.next

            right = pre.next
            pre.next = None
            return merge(sortfunc(head), sortfunc(right))

        def merge(h1,h2):
            h = ListNode()
            tailh = h
            p = h1
            q = h2
            while p is not None and q is not None:
                if p.val < q.val:
                    tailh.next = p
                    p = p.next
                    tailh = tailh.next
                else:
                    tailh.next = q
                    q = q.next
                    tailh = tailh.next

            if p is not None:
                tailh.next = p
            if q is not None:
                tailh.next = q
            return h.next

        return sortfunc(head)




