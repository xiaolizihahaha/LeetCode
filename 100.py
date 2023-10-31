# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False

        if p.val != q.val:
            return False
        if self.isSameTree(p.left,q.left) is False or self.isSameTree(p.right,q.right) is False:
            return False

        return True
