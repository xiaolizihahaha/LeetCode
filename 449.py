# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        post = ''
        if root is None:
            return post
        else:
            post += str(root.val)
            if root.left is not None:
                post += ' '
                post += self.serialize(root.left)
            if root.right is not None:
                post += ' '
                post += self.serialize(root.right)

            return post



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        pre1 = data.split(' ')
        pre = [int(p) for p in pre1]
        middle = sorted(pre)
        # print(pre)
        # print(middle)

        root = self.createTree(pre,middle)
        return root

    def createTree(self,pre,middle):
        if len(pre) == 1:
            root = TreeNode(pre[0])
            return root
        if len(pre) == 0:
            return None
        else:
            root = TreeNode(pre[0])
            index = middle.index(pre[0])
            if index >= 1:
                root.left = self.createTree(pre[1:index+1],middle[:index])
            if len(pre) - index >= 1:
                root.right = self.createTree(pre[index+1:],middle[index+1:])

            return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans