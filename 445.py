# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #新反转链表旧节点 新sum链表 新节点
        # head1 = ListNode()
        # head2 = ListNode()
        #
        # head1.next = l1
        # head2.next = l2
        #
        # p = l1
        # q = l2
        #
        # p1 = head1
        # p2 = head2
        #
        # while l1 is not None:
        #     p = l1
        #     l1 = l1.next
        #     p.next = None
        #
        #     h1next = head1.next
        #     head1.next = p
        #     p.next = h1next
        #
        # while l2 is not None:
        #     q = l2
        #     l2 = l2.next
        #     q.next = None
        #
        #     h2next = head2.next
        #     head2.next = q
        #     q.next = h2next
        #
        # p2 = head1.next
        # q2 = head2.next
        #
        # carry = 0
        # head3 = ListNode()
        # k2 = head3
        # while p2 is not None and q2 is not None:
        #     ben = p2.val + q2.val + carry
        #     carry = int(ben / 10)
        #     ben = ben % 10
        #
        #     newnode = ListNode(ben)
        #     k2.next = newnode
        #     k2 = k2.next
        #     p2 = p2.next
        #     q2 = q2.next
        #
        # while p2 is not None:
        #     ben = p2.val + carry
        #     carry = int(ben / 10)
        #     ben = ben % 10
        #
        #     newnode = ListNode(ben)
        #     k2.next = newnode
        #     k2 = k2.next
        #     p2 = p2.next
        #
        # while q2 is not None:
        #     ben = q2.val + carry
        #     carry = int(ben / 10)
        #     ben = ben % 10
        #
        #     newnode = ListNode(ben)
        #     k2.next = newnode
        #     k2 = k2.next
        #     q2 = q2.next
        #
        # if carry == 1:
        #     newnode = ListNode(1)
        #     k2.next = newnode
        #     k2 = k2.next
        #
        # k = head3
        # head4 = ListNode()
        #
        # while head3 is not None:
        #     k = head3
        #     head3 = head3.next
        #     k.next = None
        #
        #     h4next = head4.next
        #     head4.next = k
        #     k.next = h4next
        #
        # return head4.next




        #新反转链表旧节点 新sum链表 旧节点
        head1 = ListNode()
        head2 = ListNode()

        ll1 = 0
        ll2 = 0

        while l1 is not None:
            p = l1
            ll1 += 1
            l1 = l1.next
            p.next = None

            h1next = head1.next
            head1.next = p
            p.next = h1next

        while l2 is not None:
            q = l2
            ll2 += 1
            l2 = l2.next
            q.next = None

            h2next = head2.next
            head2.next = q
            q.next = h2next

        p2 = head1.next
        q2 = head2.next

        carry = 0

        #变l2 q

        if ll1 <= ll2:
            pre2 = head2.next
            while p2 is not None and q2 is not None:
                ben = p2.val + q2.val + carry
                carry = int(ben / 10)
                ben = ben % 10


                q2.val = ben
                pre2 = q2

                p2 = p2.next
                q2 = q2.next

            while q2 is not None:
                ben = q2.val + carry
                carry = int(ben / 10)
                ben = ben % 10

                q2.val = ben
                pre2 = q2

                q2 = q2.next



            if carry == 1:
                newnode = ListNode(1)
                pre2.next = newnode


            head3 = head2.next
        else:
            pre2 = head1.next
            while p2 is not None and q2 is not None:
                ben = p2.val + q2.val + carry
                carry = int(ben / 10)
                ben = ben % 10


                p2.val = ben
                pre2 = p2

                p2 = p2.next
                q2 = q2.next

            while p2 is not None:
                ben = p2.val + carry
                carry = int(ben / 10)
                ben = ben % 10

                p2.val = ben
                pre2 = p2

                p2 = p2.next

            if carry == 1:
                newnode = ListNode(1)
                pre2.next = newnode
    

            head3 = head1.next


        head4 = ListNode()

        while head3 is not None:
            k = head3
            head3 = head3.next
            k.next = None

            h4next = head4.next
            head4.next = k
            k.next = h4next

        return head4.next




