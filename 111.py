# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)
        #
        # if left == 1:
        #     return right
        # if right == 1:
        #     return left
        return min(left,right)
