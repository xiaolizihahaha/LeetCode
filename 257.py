# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if root is None:
            return []
        else:
            results = self.paths(root,'')
            return results

    def paths(self,root,path):
        results = []
        if root is not None:
            if root.left is None and root.right is None:
                path += str(root.val)
                results.append(path)
            else:
                path += str(root.val)
                path += '->'

            if root.left is not None:
                results.extend(self.paths(root.left,path))
            if root.right is not None:
                results.extend(self.paths(root.right,path))

        return results

