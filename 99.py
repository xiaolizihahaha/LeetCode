# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = self.middle(root)

        first1 = -1
        first2 = -1
        second1 = -1
        second2 = -1
        for i in range(1,len(nodes)):
            if nodes[i-1].val > nodes[i].val:
                if first1 == -1:
                    first1 = i-1
                    first2 = i
                else:
                    second1 = i-1
                    second2 = i

        if second1 == -1:
            temp = nodes[first1].val
            nodes[first1].val = nodes[first2].val
            nodes[first2].val = temp
        else:
            temp = nodes[first1].val
            nodes[first1].val = nodes[second2].val
            nodes[second2].val = temp



    def middle(self, root):
        if root is None:
            return []
        else:
            l = self.middle(root.left)
            l.append(root)
            l.extend(self.middle(root.right))
            return l
