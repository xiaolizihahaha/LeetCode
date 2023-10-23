class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """


        for i in range(9):
            numlist = [0,0,0,0,0,0,0,0,0,0]
            for j in range(9):
                if board[i][j] !='.':
                    if numlist[int(board[i][j])] == 0:
                        numlist[int(board[i][j])] = 1
                    else :
                        # print(i, j)
                        result = False
                        return result

        for j in range(9):
            numlist = [0,0,0,0,0,0,0,0,0,0]
            for i in range(9):
                if board[i][j] !='.':
                    if numlist[int(board[i][j])] == 0:
                        numlist[int(board[i][j])] = 1
                    else :
                        # print(i,j)
                        result = False
                        return result


        for i in [0,3,6]:
            for j in [0,3,6]:

                numlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                if board[i][j] !='.':
                    if numlist[int(board[i][j])] == 0:
                        numlist[int(board[i][j])] = 1
                    else :
                        result = False
                        return result


                # board[i][j+1]
                if board[i][j+1] !='.':
                    if numlist[int(board[i][j+1])] == 0:
                        numlist[int(board[i][j+1])] = 1
                    else :
                        result = False
                        return result
                # board[i][j+2]
                if board[i][j+2] !='.':
                    if numlist[int(board[i][j+2])] == 0:
                        numlist[int(board[i][j+2])] = 1
                    else :
                        result = False
                        return result

                # board[i+1][j]
                if board[i+1][j] !='.':
                    if numlist[int(board[i+1][j])] == 0:
                        numlist[int(board[i+1][j])] = 1
                    else :
                        result = False
                        return result

                # board[i+1][j+1]
                if board[i+1][j+1] !='.':
                    if numlist[int(board[i+1][j+1])] == 0:
                        numlist[int(board[i+1][j+1])] = 1
                    else :
                        result = False
                        return result

                # board[i+1][j+2]
                if board[i+1][j+2] !='.':
                    if numlist[int(board[i+1][j+2])] == 0:
                        numlist[int(board[i+1][j+2])] = 1
                    else :
                        result = False
                        return result

                # board[i+2][j]
                if board[i+2][j] !='.':
                    if numlist[int(board[i+2][j])] == 0:
                        numlist[int(board[i+2][j])] = 1
                    else :
                        result = False
                        return result

                # board[i+2][j+1]
                if board[i+2][j+1] !='.':
                    if numlist[int(board[i+2][j+1])] == 0:
                        numlist[int(board[i+2][j+1])] = 1
                    else :
                        result = False
                        return result

                # board[i+2][j+2]
                if board[i+2][j+2] !='.':
                    if numlist[int(board[i+2][j+2])] == 0:
                        numlist[int(board[i+2][j+2])] = 1
                    else :
                        result = False
                        return result


        result = True
        return  result


if __name__ == '__main__':
    # board =[["5", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    # board =[["8", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
             [".", "4", ".", "3", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", "3", ".", ".", "1"],
             ["8", ".", ".", ".", ".", ".", ".", "2", "."],
             [".", ".", "2", ".", "7", ".", ".", ".", "."],
             [".", "1", "5", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", "2", ".", ".", "."],
             [".", "2", ".", "9", ".", ".", ".", ".", "."],
             [".", ".", "4", ".", ".", ".", ".", ".", "."]]

    solution = Solution()
    result = solution.isValidSudoku(board)
    print(result)
