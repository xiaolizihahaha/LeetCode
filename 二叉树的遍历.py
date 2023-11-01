import copy


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Traversel(object):
    #前序遍历
    def preOrderTraversel(self,root):
        print(root.val)
        self.preOrderTraversel(root.left)
        self.preOrderTraversel(root.right)
    # 中序遍历
    def inOrderTraversel(self,root):
        self.inOrderTraversel(root.left)
        print(root.val)
        self.inOrderTraversel(root.right)

    #后序遍历
    def postOrderTraversel(self,root):
        self.postOrderTraversel(root.left)
        self.postOrderTraversel(root.right)
        print(root.val)

    #广度遍历
    def levelTraverse(self,root):
        if root is None:
            return
        l = []
        l.append(root)
        while len(l) != 0:
            out = l.pop(0)
            print(out.val)
            if out.left is not None:
                l.append(out.left)
            if out.right is not None:
                l.append(out.right)

    #层序遍历且分层输出元素
    def levelTraverse1(self, root):
        if root is None:
            return
        l = []
        l.append(root)
        while len(l) != 0 :
            listsize = len(l)
            for i in range(listsize):
                out = l.pop(0)
                print(out.val)

                if out.left is not None:
                    l.append(out.left)
                if out.right is not None:
                    l.append(out.right)
            print('下一层')


    #深度遍历
    def depthOrderTraverse(self,root):
        if root is None:
            return
        l = []
        l.append(root)
        while len(l) != 0:
            out = l.pop(0)
            print(out.val)
            if out.left is not None:
                l.insert(0,out.left)
            if out.right is not None:
                l.insert(0,out.right)

    #深度遍历节点 输出root到叶子的每条路径
    def depthOrderPath(self,root):
        if root is None:
            return []
        else:
            return self.path(root,[])

    def path(self,root,path):
        paths = []
        if root is not None:
            path.append(root.val)
            if root.left is None and root.right is None:
                paths.append(copy.deepcopy(path))
            if root.left is not None:
                paths.extend(self.path(root.left,copy.deepcopy(path)))
            if root.right is not None:
                paths.extend(self.path(root.right,copy.deepcopy(path)))

        return paths


