class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        hang = []
        lie =[]
        for i in range(len(matrix)):
            if matrix[i].count(0) !=0 :
              hang.append(i)


        for i in range(len(matrix[0])):
            matrixj = [example[i] for example in matrix]
            if matrixj.count(0) != 0:
                lie.append(i)

        for h in hang:
            for i in range(len(matrix[0])):
                matrix[h][i] = 0

        for l in lie:
            for i in range(len(matrix)):
                matrix[i][l] = 0




if __name__ == '__main__':
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    #
    # matrix = [[0, 1, 2, 0],
    #           [3, 4, 5, 2],
    #           [1, 3, 1, 5]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)