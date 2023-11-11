class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """

        results = list()


        self.dfs(n,'',results,0)
        # print(results)
        for i in range(len(results)):
            results[i] = int(results[i],2)

        index = results.index(start)
        re = results[index:]
        re.extend(results[:index])

        print(re)
        return re


    def dfs(self,n,path,results,x):
        if len(path) == n:
            results.append(path[:])
            return

        if x == 0:
            self.dfs(n,path + '0',results,0)
            self.dfs(n,path + '1',results,1)
        else:
            self.dfs(n,path + '1',results,0)
            self.dfs(n,path + '0',results,1)


if __name__ == '__main__':
    n = 2
    start = 3

    n = 3
    start = 2
    solution = Solution()
    solution.circularPermutation(n,start)


