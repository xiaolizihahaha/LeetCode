class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        p = 0
        q = 0
        ans = list()

        while p <= len(mat) - 1 or q <= len(mat[0]) - 1:
            if q == 0 or p == len(mat) - 1:
                while p != -1 and q < len(mat[0]):
                    ans.append(mat[p][q])
                    p = p - 1
                    q = q + 1

                p = p + 1
                q = q - 1

                if q == len(mat[0]) - 1:
                    p = p + 1
                else:
                    q = q + 1


            if p == 0 or q == len(mat[0]) - 1:
                while q != -1 and p < len(mat):
                    ans.append(mat[p][q])
                    p = p + 1
                    q = q - 1

                p = p - 1
                q = q + 1

                if p == len(mat) - 1:
                    q = q + 1
                else:
                    p = p + 1

        print(ans)
        return ans



if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]]
    solution = Solution()
    solution.findDiagonalOrder(mat)



