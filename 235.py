# Definition for a binary tree node.
import copy


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#先找到 到p、q的路径，然后对比路径 找到最近祖先节点——————超时（要注意这个二叉树是一个二叉搜索树！！！，可以很方便的找到路径，不需要深度遍历）
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         if root is None:
#             return None
#
#         ppath= self.seakPath(root,p,[])
#         qpath = self.seakPath(root,q,[])
#
#         same = list()
#
#         for i,j in zip(ppath,qpath):
#             if i.val == j.val:
#                 same.append(i)
#             else:
#                 break
#
#         return same[-1]
#
#
#
#     def seakPath(self,root,p,path):
#         if root is not None:
#             path.append(root)
#         if root == p:
#             return copy.deepcopy(path)
#
#         if root.left is not None:
#             if self.seakPath(root.left,p,copy.deepcopy(path)) is not None:
#                 return self.seakPath(root.left,p,copy.deepcopy(path))
#         if root.right is not None:
#             if self.seakPath(root.right,p,copy.deepcopy(path)) is not None:
#                 return self.seakPath(root.right,p,copy.deepcopy(path))
#
#         return


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        ppath = self.seak(root,p,'')
        qpath = self.seak(root,q,'')
        same = list()

        ppath1 = ppath.split(' ')
        ppath1.pop(-1)
        qpath1 = qpath.split(' ')
        qpath1.pop(-1)

        # print(ppath1)
        # print(qpath1)

        for i,j in zip(ppath1,qpath1):
            if i == j:
                same.append(i)
            else:
                break

        goal = same[-1]
        print(goal)

        k = root
        while k != None:
            if int(goal) < k.val:
                k = k.left
            elif int(goal) > k.val:
                k = k.right
            else:
                break


        return k


    def seak(self,root,p,path):
        if root is None:
            return ''
        else:
            path += str(root.val)
            path += ' '
            if root == p:
                return path


        if p.val < root.val:
            return self.seak(root.left,p,path)
        else:
            return self.seak(root.right,p,path)



