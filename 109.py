# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """

        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        llen = 0
        p = head
        while p is not None:
            llen += 1
            p = p.next

        middle = int(llen / 2)
        i = 0
        p = head

        leftone = head
        while i < middle - 1:
            i += 1
            p = p.next

        middleone = p.next
        p.next = None

        rightone = middleone.next
        middleone.next = None

        root = TreeNode(middleone.val)
        root.left = self.sortedListToBST(leftone)
        root.right = self.sortedListToBST(rightone)

        return root

