# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None and root.left is None and root.right is None:
            return 0

        sum = 0
        left = root.left

        if left is not None and left.left is None and left.right is None:
            sum += left.val
        if root.left is not None:
            sum += self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            sum += self.sumOfLeftLeaves(root.right)

        return sum


