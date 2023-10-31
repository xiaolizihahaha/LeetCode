# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = list()
        queue = list()
        queue1 = list()
        if root is None:
            return []

        queue.append(root)
        queue1.append(root.val)


        while len(queue) != 0:
            perfloor = len(queue)
            result.append(copy.deepcopy(queue1))
            for i in range(perfloor):
                out = queue.pop(0)
                queue1.pop(0)
                if out.left is not None:
                    queue.append(out.left)
                    queue1.append(out.left.val)
                if out.right is not None:
                    queue.append(out.right)
                    queue1.append(out.right.val)



        return result