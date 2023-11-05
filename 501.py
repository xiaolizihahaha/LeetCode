# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = list()

        l = self.findMode(root)
        d = dict()

        ss = set(l)

        for s in ss:
            if d.get(s) is None:
                d[s] = l.count(s)

        print(d)
        maxval = -1
        for key in d:
            if d[key] >= maxval:
                maxval = d[key]

        result = list()

        for key in d:
            if d[key] == maxval:
                result.append(key)

        return result

    def preorder(self,root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        l = list()
        if root.left is not None:
            l.extend(self.preorder(root.left))
        l.append(root.val)
        if root.right is not None:
            l.extend(self.preorder(root.right))

        return l