# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        left = self.treedeep(root.left)
        right = self.treedeep(root.right)

        if abs(left - right) > 1:
            return False
        if self.isBalanced(root.left) is False or self.isBalanced(root.right) is False:
            return False

        return True

    def treedeep(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        left = 1 + self.treedeep(root.left)
        right = 1 + self.treedeep(root.right)

        return max(left, right)

