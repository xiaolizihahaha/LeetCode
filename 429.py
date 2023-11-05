import copy


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = list()
        result = list()
        queue1 = list()
        queue.append(root)
        queue1.append(root.val)

        while len(queue) != 0:
            floorsize = len(queue)
            result.append(copy.deepcopy(queue1))
            for i in range(floorsize):
                out = queue.pop(0)
                queue1.pop(0)
                for c in out.children:
                    queue.append(c)
                    queue1.append(c.val)
        print(result)
        return result

