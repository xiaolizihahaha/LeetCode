# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        # 超时了的，为啥？
        # 因为我去找了左子树的最小值，右子树的最大值。还找了左子树的左子树的最小值，左子树的右子树的最大值，右子树的左子树的最小值，右子树的右子树的最大值。。。。每个节点都找了一次
        # 不如规定范围
# class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root is None:
    #         return True
    #     if root.left is None and root.right is None:
    #         return True
    #
    #     left = root.left
    #     right = root.right
    #     if left is not None and root.val <= self.maxof(left):
    #         print('aaaa',root)
    #         return False
    #     if right is not None and root.val >= self.minof(right):
    #         print('bbbb',root,self.minof(right))
    #         return False
    #
    #     if self.isValidBST(left) is False or self.isValidBST(right) is False:
    #         print('cccc',root)
    #         return False
    #
    #     return True
    #
    # def maxof(self,root):
    #     left = -1 * (math.pow(2,32)-1)
    #     right = -1 * (math.pow(2,32)-1)
    #     if root is None:
    #         return -1 * (math.pow(2,32)-1)
    #     if root.left is None and root.right is None:
    #         return root.val
    #     if root.left is not None:
    #         left = self.maxof(root.left)
    #     if root.right is not None:
    #         right = self.maxof(root.right)
    #     return max(left,right,root.val)
    # def minof(self,root):
    #     left = math.pow(2,32)
    #     right = math.pow(2,32)
    #     if root is None:
    #         return math.pow(2,32)
    #     if root.left is None and root.right is None:
    #         return root.val
    #     if root.left is not None:
    #         left =  self.minof(root.left)
    #         print('lll',left)
    #     if root.right is not None:
    #         right = self.minof(root.right)
    #         print('rrr', right)
    #     return min(left,right,root.val)

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        else:
            return self.judge(root,(-1) * math.pow(2,31) - 1, math.pow(2,31))

    def judge(self, root,min,max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        left = root.left
        right = root.right
        if self.judge(left,min,root.val) and self.judge(right,root.val,max):
            return True
        else:
            return False