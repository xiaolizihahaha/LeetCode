# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.middle = list()
        self.middle.append(-1)
        self.middle.extend(self.middleOrder(root))
        self.current = 0

    def next(self):
        """
        :rtype: int
        """
        self.current += 1
        return self.middle[self.current]


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.current < len(self.middle) - 1:
            return True
        else:
            return False

    def middleOrder(self, root):
        results = list()
        if root is None:
            return []
        results.extend(self.middleOrder(root.left))
        results.append(root.val)
        results.extend(self.middleOrder(root.right))

        return results

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()