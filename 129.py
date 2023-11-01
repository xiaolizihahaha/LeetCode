# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            paths = self.path(root,'')
            sums = 0
            for path in paths:
                result = int(path)
                sums += result

            return sums

    def path(self,root,path):
        paths = []
        if root is not None:
            path += str(root.val)

            if root.left is None and root.right is None:
                paths.append(path)

            if root.left is not None:
                paths.extend(self.path(root.left,path))
            if root.right is not None:
                paths.extend(self.path(root.right,path))

        return paths

