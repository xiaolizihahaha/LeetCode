# Definition for a binary tree node.
import copy


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder) == 1 and len(inorder) == 1:
            tree = TreeNode(val=preorder[0])
            tree.left = None
            tree.right = None
            print(preorder[0],"yeyeyeye")

        else:
            tree = TreeNode(val = preorder[0])
            print(preorder[0])
            index = inorder.index(preorder[0])

            if index != 0 :
                tree.left = self.buildTree(preorder[1:index + 1], inorder[0:index])
            else :
                tree.left = None
            if len(inorder) - index - 1 != 0:
                tree.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
            else :
                tree.right = None

        return tree

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # 输出: [3, 9, 20, null, null, 15, 7]



    # preorder = [-1]
    # inorder = [-1]
    # 输出: [-1]

    # preorder = [1,2]
    # inorder = [2,1]

    solution = Solution()
    tree = solution.buildTree(preorder,inorder)
    print(tree)
