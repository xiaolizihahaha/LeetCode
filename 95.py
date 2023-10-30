# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        else:
            return self.generateTree(1, n)
    def generateTree(self,start,end):
        result = []
        if start > end :
            result.append(None)
            return result
        if start == end:
            newnode = TreeNode(start)
            result.append(newnode)
            return result
        for i in range(start,end+1):
            left = self.generateTree(start,i-1)
            right = self.generateTree(i+1,end)


            for l in left:
                for r in right:
                    newnode = TreeNode(i)
                    newnode.left = l
                    newnode.right = r
                    result.append(newnode)

        return result


