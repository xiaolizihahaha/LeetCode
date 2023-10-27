
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
        l = list()
        l.append(root)
        while len(l) != 0:
            listsize = len(l)
            pre = None
            for i in range(listsize):
                out = l.pop(0)
                if pre is not None:
                    pre.next = out
                pre = out
                if out.left is not None:
                    l.append(out.left)
                if out.right is not None:
                    l.append(out.right)

        return root

