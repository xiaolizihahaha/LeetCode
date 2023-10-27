
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if root is None:
            return

        leftone = root.left
        rightone = root.right
        if leftone is None and rightone is None:
            root.next = None
            return root

        root.next = None
        # leftone.next = rightone
        # rightone.next = None

        self.connect(leftone)
        self.connect(rightone)

        p = leftone
        q = rightone
        while p is not None and q is not None:
            p.next = q
            p = p.right
            q = q.left




        return root