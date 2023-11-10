class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        results = list()
        self.dfs(graph,[0],results,0)

        print(results)
        return results
    def dfs(self,gragh,path,results,index):
        if path[-1] == len(gragh)-1:
            results.append(path[:])
            return

        for i in gragh[index]:
            path.append(i)
            self.dfs(gragh,path,results,i)
            path.pop(-1)



if __name__ == '__main__':
    # graph = [[1, 2],
    #          [3],
    #          [3],
    #          []]
    # [[0, 1, 3], [0, 2, 3]]

    graph = [[4, 3, 1],
             [3, 2, 4],
             [3],
             [4],
             []]
    # [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]

    solution = Solution()
    solution.allPathsSourceTarget(graph)