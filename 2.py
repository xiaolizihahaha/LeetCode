class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None and l2 == None:
            return None

        head3 = ListNode(0)
        pre = head3

        temp = 0
        while l1 and l2 :
            value = l1.val + l2.val + temp
            pre.next = ListNode(value % 10)
            temp = int (value / 10)
            pre = pre.next
            l1 = l1.next
            l2 = l2.next

        while l1 :
            value = l1.val + temp
            pre.next = ListNode(value % 10)
            temp = int(value / 10)
            pre = pre.next
            l1 = l1.next

        while l2:
            value = l2.val + temp
            pre.next = ListNode(value % 10)
            temp = int(value / 10)
            pre = pre.next
            l2 = l2.next

        if temp > 0:
            pre.next = ListNode(1)
            pre = pre.next

        l3 = head3.next
        return l3





if __name__ == '__main__':
    num1 = 9999999
    num2 = 9999
    result = num1 + num2

    # print(result)

    head1 = ListNode(0)
    pre = head1
    for n in str(num1)[::-1]:
        pre.next = ListNode(int(n))
        pre = pre.next

    l1 = head1.next

    head2 = ListNode(0)
    pre2 = head2
    for n in str(num2)[::-1]:
        pre2.next = ListNode(int(n))
        pre2 = pre2.next
    l2 = head2.next

    solution = Solution()


    point = solution.addTwoNumbers(l1,l2)
    while(point):
        print("hhs",point.val)
        point = point.next

