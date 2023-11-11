class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        results = list()
        r = 0
        for g in grid:
            g.insert(0,0)
            g.append(0)
        length = len(grid[0])
        grid.insert(0,[0] * length)
        grid.append([0] * length)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    # print(i,j,grid[i][j])
                    self.dfs(grid,i,j,[grid[i][j]],results)

        # print(results)
        if len(results) == 0:
            # print([])
            return 0
        else:
            # print(sum(results[0]))
            return sum(results[0])



    def dfs(self,grid,i,j,path,results):
        if grid[i-1][j] == 0 and grid[i+1][j] == 0 and grid[i][j+1] == 0 and grid[i][j-1] == 0:
            if len(results) == 0:
                results.append(path[:])
            else:
                if sum(path) > sum(results[0]):
                    results[0] = path[:]
            return


        if grid[i-1][j] != 0:
            path.append(grid[i-1][j])
            temp = grid[i][j]
            grid[i][j] = 0
            self.dfs(grid,i-1,j,path,results)
            path.pop(-1)
            grid[i][j] = temp


        if grid[i][j+1] != 0:
            path.append(grid[i][j+1])
            temp = grid[i][j]
            grid[i][j] = 0
            self.dfs(grid,i,j+1,path,results)
            path.pop(-1)
            grid[i][j] = temp

        if grid[i+1][j] != 0:
            path.append(grid[i + 1][j])
            temp = grid[i][j]
            grid[i][j] = 0
            self.dfs(grid, i + 1, j, path, results)
            path.pop(-1)
            grid[i][j] = temp


        if grid[i][j-1] != 0:
            path.append(grid[i][j-1])
            temp = grid[i][j]
            grid[i][j] = 0
            self.dfs(grid,i,j-1,path,results)
            path.pop(-1)
            grid[i][j] = temp





if __name__ == '__main__':
    grid = [[0, 6, 0],
            [5, 8, 7],
            [0, 9, 0]]

    grid = [[1, 0, 7],
            [2, 0, 6],
            [3, 4, 5],
            [0, 3, 0],
            [9, 0, 20]]

    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    solution = Solution()
    solution.getMaximumGold(grid)

