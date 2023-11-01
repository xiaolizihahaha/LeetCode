# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        if root is None:
            return []

        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)

        return result