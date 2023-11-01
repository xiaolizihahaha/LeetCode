# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        if root is None:
            return []

        result.append(root.val)

        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))

        return result