# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = list()
        treenode = list()
        treeval = list()


        if root is None:
            return []
        treenode.append(root)
        treeval.append(root.val)

        while len(treenode) != 0:
            perfloor = len(treenode)
            result.append(copy.deepcopy(treeval))

            for i in range(perfloor):
                out = treenode.pop(0)
                treeval.pop(0)
                if out.left is not None:
                    treenode.append(out.left)
                    treeval.append(out.left.val)
                if out.right is not None:
                    treenode.append(out.right)
                    treeval.append(out.right.val)

        return result[::-1]



