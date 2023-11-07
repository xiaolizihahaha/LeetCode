# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if root is None:
            return 0

        chooses = self.getChoose(root)
        print(chooses)
        num = 0
        for choose in chooses:
            for c in choose:
                if c == targetSum:
                    num += 1

        return num


    # def getChoose(self,root):
    #     if root.left is None and root.right is None:
    #         return [root.val]
    #     else:
    #         result = list()
    #         result.append(root.val)
    #
    #         if root.left is not None:
    #             ls = self.getChoose(root.left)
    #             for l in ls:
    #                 result.append(root.val + l)
    #         if root.right is not None:
    #             rs = self.getChoose(root.right)
    #             for r in rs:
    #                 result.append(root.val + r)
    #         return result
    def getChoose(self,root):
        paths = []
        if root.left is None and root.right is None:
            paths.append([root.val])
            return paths
        else:
            result = list()
            result.append(root.val)

            if root.left is not None:
                ls = self.getChoose(root.left)
                paths.extend(ls)
                for l in ls[-1]:
                    result.append(root.val + l)
            if root.right is not None:
                rs = self.getChoose(root.right)
                paths.extend(rs)
                for r in rs[-1]:
                    result.append(root.val + r)
            paths.append(result)
            return paths

