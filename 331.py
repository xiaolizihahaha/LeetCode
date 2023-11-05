import copy


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        preorder1 = preorder.split(',')
        pre = list()
        # print(preorder1)

        while len(pre) != len(preorder1) and len(preorder1) > 2:
            i = 0
            pre = copy.deepcopy(preorder1)
            while i < len(preorder1) - 2:
                if preorder1[i] != '#' and preorder1[i+1] == '#' and preorder1[i+2] == '#':
                    preorder1[i] = '#'
                    preorder1.pop(i+2)
                    preorder1.pop(i+1)
                i += 1

            print(preorder1)

        if len(preorder1) == 1 and preorder1[0] == '#':
            return True
        else:
            return False


if __name__ == '__main__':
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    # preorder = "1,#"
    # preorder = "9,#,#,1"
    solution = Solution()
    solution.isValidSerialization(preorder)
