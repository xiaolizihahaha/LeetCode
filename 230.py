# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        queue = list()
        total = list()

        queue.append(root)
        while len(queue) != 0:
            out = queue.pop(0)
            total.append(out.val)

            if out.left is not None:
                queue.append(out.left)
            if out.right is not None:
                queue.append(out.right)

        total.sort()
        return total[k-1]

# if __name__ == '__main__':
    # l = [1,2,3]
    # print(l[-3])
