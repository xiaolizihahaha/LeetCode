# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None and root.right is not None:
            return False
        if root.left is not None and root.right is None:
            return False
        if root.left.val != root.right.val:
            return False
        left = root.left
        right = root.right

        if self.cmp(left,right) is True:
            return True
        else:
            return False
    def cmp(self,left,right):

        if left is None and right is None:
            return True
        if left is not None and right is None:
            return False
        if left is None and right is not None:
            return False
        if left.val != right.val:
            return False

        # if left.left is None and right.right is None:

        if left.left is not None and right.right is None:
            return False
        if left.left is None and right.right is not None:
            return False

        if left.left is not None and right.right is not None and left.left.val != right.right.val:
            return False

        # if left.right is None and right.left is None:

        if left.right is not None and right.left is None:
            return False
        if left.right is None and right.left is not None:
            return False
        if left.right is not None and right.left is not None and left.right.val != right.left.val:
            return False

        if self.cmp(left.left,right.right)is False or self.cmp(left.right,right.left) is False:
            return False
        return True


