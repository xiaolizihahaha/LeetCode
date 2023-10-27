# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # if root is None:
        #     return None
        # if root.left is None and root.right is None:
        #
        #     newnode = TreeNode(root.val)
        #     newnode.left = None
        #     newnode.right = None
        #     return newnode
        #
        # root1 = TreeNode(root.val)
        # root1.left = None
        # leftone = root.left
        # rightone = root.right
        # root1.right = self.flatten(leftone)
        # p = root1
        # while p.right is not None:
        #     p = p.right
        # p.left = None
        # p.right = self.flatten(rightone)
        #
        # root = root1


        # #原树上做修改
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root

        leftone = root.left
        rightone = root.right

        root.left = None
        root.right = self.flatten(leftone)
        p = root
        while p.right is not None:
            p = p.right
        p.left = None
        p.right = self.flatten(rightone)

        return root