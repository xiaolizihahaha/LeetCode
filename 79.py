class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # print(xs,ys)

        for bo in board:
            bo.insert(0,'1')
            bo.append('1')

        board.insert(0,['1']*len(board[0]))
        board.append(['1']*len(board[0]))


        xs = list()
        ys = list()

        for i,bo in enumerate(board):
            for j,b in enumerate(bo):
                if b == word[0]:
                    xs.append(i)
                    ys.append(j)

        result = list()
        for x,y in zip(xs,ys):
            # print(x,y)
            path = list()
            path.append(str(x) + ',' + str(y))
            # print(path)
            self.traceBack(board,word[1:],x,y,path,result)

        if 1 in result:
            return True
        else:
            return False
        # return result

    def traceBack(self,board,word,x,y,path,result):
        # print(word,x,y)
        if len(word) == 0:
            result.append(1)
            return

        if board[x-1][y] != word[0] and board[x+1][y] != word[0] and board[x][y-1] != word[0] and board[x][y+1] !=word[0]:
            return

        if board[x-1][y] == word[0]:
            newstr = str(x-1) + ',' + str(y)
            if newstr not in path:
                path.append(str(x-1) + ',' + str(y))
                self.traceBack(board,word[1:],x-1,y,path,result)
                path.pop(-1)

        if board[x+1][y] == word[0]:
            newstr = str(x+1) + ',' + str(y)
            if newstr not in path:
                path.append(str(x + 1) + ',' + str(y))
                self.traceBack(board,word[1:],x+1,y,path,result)
                path.pop(-1)

        if board[x][y-1] == word[0]:
            newstr = str(x) + ',' + str(y-1)
            if newstr not in path:
                path.append(str(x) + ',' + str(y-1))
                self.traceBack(board,word[1:],x,y-1,path,result)
                path.pop(-1)

        if board[x][y+1] == word[0]:
            newstr = str(x) + ',' + str(y+1)
            if newstr not in path:
                path.append(str(x) + ',' + str(y+1))
                self.traceBack(board,word[1:],x,y+1,path,result)
                path.pop(-1)

if __name__ == '__main__':
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCED"

    #
    # board = [["A", "B", "C", "E"],
    #          ["S", "F", "C", "S"],
    #          ["A", "D", "E", "E"]]
    # word = "SEE"
    #
    # board = [["A", "B", "C", "E"],
    #          ["S", "F", "C", "S"],
    #          ["A", "D", "E", "E"]]
    # word = "ABCB"

    # print(len(w))

    solution = Solution()
    solution.exist(board,word)
