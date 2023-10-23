
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            head1 = None
            return head1

        head1 = Node(head.val)
        pre1 =head1
        pre = head

        suo = []
        suo1 = []

        suo.append(head)
        suo1.append(head1)

        while pre.next != None:
            pre1.val = pre.val
            nextnode = Node(pre.next.val)
            pre1.next = nextnode

            suo.append(pre.next)
            suo1.append(pre1.next)

            pre = pre.next
            pre1 = pre1.next

        pre1.next = None

        pre3 = head1
        pre2 = head

        while pre2 != None:
            if pre2.random == None:
                pre3.random = None
            else:
                pre3.random = suo1[suo.index(pre2.random)]





            pre2 = pre2.next
            pre3 = pre3.next


        return head1











if __name__ == '__main__':
    # head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]

    # head = [[1, 1], [2, 1]]
    #
    # head = [[3, null], [3, 0], [3, null]]


    solution = Solution()
    solution.copyRandomList(head)