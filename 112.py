# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        else:
            paths = self.path(root,[])
            print(paths)
            sums = list()
            for path in paths:
                sum1 = sum(path)
                sums.append(sum1)
            if targetSum in sums:
                return True
            else:
                return False

    def path(self,root,path):
        paths = list()

        if root is not None:
            path.append(root.val)
            if root.left is None and root.right is None:
                paths.append(copy.deepcopy(path))

            if root.left is not None:
                paths.extend(self.path(root.left,copy.deepcopy(path)))
            if root.right is not None:
                paths.extend(self.path(root.right,copy.deepcopy(path)))

        return paths




