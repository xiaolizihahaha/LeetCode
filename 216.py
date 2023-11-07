class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = list()

        self.dfs(k,n,[],results,0)
        re = list()
        for result in results:
            result.sort()
            if result not in re:
                re.append(result)
        print(re)
        return re

    def dfs(self,k,n,path,results,time):
        if time == k and n == 0:
            results.append(path[:])
            return

        for i in range(1,10):
            if i not in path:
                r1 = i
                r1r = n-i
                if r1r >= k-1-time:
                    path.append(r1)
                    self.dfs(k,r1r,path,results,time+1)
                    path.pop(-1)

if __name__ == '__main__':
    # k = 3
    # n = 7
    #
    # k = 3
    # n = 9
    #
    k = 4
    n = 1
    solution = Solution()
    solution.combinationSum3(k,n)