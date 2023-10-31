# Definition for a binary tree node.
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
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
            else:
                return False

        queue = list()
        queue1 = list()
        result = list()
        queue.append(root)

        while len(queue) > 0:
            out = queue.pop(0)
            queue1.append(out.val)

            if out.right is not None:
                queue.insert(0,out.right)
            if out.left is not None:
                queue.insert(0,out.left)

            if out.left is None and out.right is None:
                result.append(sum(queue1))
                queue1.pop(-1)
        print(result)

        if targetSum in result:
            return True
        else:
            return False



