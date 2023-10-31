# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            newnode = TreeNode(nums[0])
            newnode.left = None
            newnode.right = None
            return newnode

        middle = int(len(nums) / 2)
        left = nums[:middle]
        right = nums[middle+1:]
        newnode = TreeNode(nums[middle])
        newnode.left = self.sortedArrayToBST(left)
        newnode.right = self.sortedArrayToBST(right)

        return newnode


if __name__ == '__main__':

    l = [1, 2]
    l.insert(0,3)
    l.pop(-1)
    print(l)
    print(l[2:])


