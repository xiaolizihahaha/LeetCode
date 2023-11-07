
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight



class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        if grid.count([1] * n) == n:
            node = Node(1,True,None,None,None,None)
            return node
        elif grid.count([0] * n) == n:
            node = Node(0,True,None,None,None,None)
            return node
        else:
            node = Node(0, False, None, None, None, None)
            half = int(n / 2)
            temp = grid[:half]
            part1 = [temp1[:half] for temp1 in temp]
            part2 = [temp1[half:] for temp1 in temp]
            temp = grid[half:]
            part3 = [temp1[:half] for temp1 in temp]
            part4 = [temp1[half:] for temp1 in temp]

            node.topLeft = self.construct(part1)
            node.topRight = self.construct(part2)
            node.bottomLeft = self.construct(part3)
            node.bottomRight = self.construct(part4)

            return node



if __name__ == '__main__':

    # grid = [[0, 1], [1, 0]]
    grid = [[1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]]
    solution = Solution()
    solution.construct(grid)


