# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = 0
        right = 0
        if root.left is not None:
            left = self.deep(root.left)
        if root.right is not None:
            right = self.deep(root.right)

        total = 1
        if left > right:
            for i in range(right):
                total += pow(2,i)

            leftnum = self.total(root.left)

            total += leftnum
            return total

        if left == right:
            for i in range(left):
                total += pow(2,i)

            rightnum = self.total(root.right)

            total += rightnum
            return total


    def deep(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        left = 1
        right = 1
        if root.left is not None:
            left = 1 + self.deep(root.left)
        if root.right is not None:
            right = 1 + self.deep(root.right)

        return max(left,right)

    def total(self,root):
        num = 0
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        queue = list()
        queue.append(root)

        while len(queue) != 0:
            out = queue.pop(0)
            num += 1
            if out.left is not None:
                queue.append(out.left)
            if out.right is not None:
                queue.append(out.right)

        return num

