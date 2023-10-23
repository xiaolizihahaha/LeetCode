# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder) == 1 and len(postorder) == 1:
            tree = TreeNode(val = postorder[-1])
            # print(postorder[-1],"yeyeye")
            tree.left = None
            tree.right = None

        else:

            index = inorder.index(postorder[-1])
            # print(postorder[-1])

            tree = TreeNode(val=postorder[-1])
            if index == 0:
                tree.left = None
            else:
                tree.left = self.buildTree(inorder = inorder[0:index], postorder = postorder[0:index])

            if len(inorder) - 1 -index == 0:
                tree.right = None
            else:
                tree.right = self.buildTree(inorder = inorder[index+1:], postorder = postorder[index:len(inorder) -1])

        return tree



if __name__ == '__main__':

    # inorder = [9, 3, 15, 20, 7]
    # postorder = [9, 15, 7, 20, 3]

    # inorder.index()
    # 输出：[3, 9, 20, null, null, 15, 7]


    inorder = [-1]
    postorder = [-1]
    # 输出：[-1]
    solution = Solution()
    tree = solution.buildTree(inorder,postorder)
    print(tree)