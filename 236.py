# Definition for a binary tree node.
import copy


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#超时 递归找到p、q节点的路径（val值），寻找最近公共祖先val，再拿着val去寻找该节点
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         ppath = self.seak(root,p,'')
#         qpath = self.seak(root,q,'')
#
#         ppath1 = ppath.split(' ')
#         qpath1 = qpath.split(' ')
#         ppath1.pop(-1)
#         qpath1.pop(-1)
#
#         # print(ppath1)
#         # print(qpath1)
#
#         same = list()
#
#         for i,j in zip(ppath1,qpath1):
#             if i == j:
#                 same.append(i)
#             else:
#                 break
#
#         goal = int(same[-1])
#
#         result = self.seakval(root,goal)
#
#         return result
#
#
#
#
#
#     def seak(self,root,p,path):
#         if root is None:
#             return ''
#         else:
#             path += str(root.val)
#             path += ' '
#             if root == p:
#                 return path
#
#             else:
#                 if root.left is not None:
#                     if self.seak(root.left,p,path) is not None:
#                         return self.seak(root.left,p,path)
#                 if root.right is not None:
#                     if self.seak(root.right,p,path) is not None:
#                         return self.seak(root.right,p,path)
#             return
#
#     def seakval(self,root,goal):
#         if root is None:
#             return None
#         if goal == root.val:
#             return root
#         if root.left is not None:
#             if self.seakval(root.left,goal) is not None:
#                 return self.seakval(root.left,goal)
#         if root.right is not None:
#             if self.seakval(root.right,goal) is not None:
#                 return self.seakval(root.right,goal)
#
#         return



#还超时  递归找到到p、q节点的路径（treenode列表）进行比较，直接找到公共最近祖先
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
#         ppath = self.seak(root,p,[])
#         qpath = self.seak(root,q,[])
#
#         same = list()
#         for i,j in zip(ppath,qpath):
#             if i.val == j.val:
#                 same.append(i)
#             else:
#                 break
#         goal = same[-1]
#         return goal
#
#     def seak(self,root,p,path):
#         if root is None:
#             return []
#         else:
#             path.append(root)
#             if root == p:
#                 return copy.deepcopy(path)
#
#             else:
#                 if root.left is not None:
#                     p1 = copy.deepcopy(path)
#                     sig1 = self.seak(root.left,p,p1)
#                     if sig1 is not None:
#                         return sig1
#                 if root.right is not None:
#                     p2 = copy.deepcopy(path)
#                     sig2 = self.seak(root.right,p,p2)
#                     if sig2 is not None:
#                         return sig2
#             return


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left is None:
            return right
        if right is None:
            return left
        if left and right:
            return root
        return

