class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        results = list()
        re = list()
        for i in range(1,10):
            # print(i)
            # print([i])
            #长度为n，相差绝对值为k
            path = ''
            path += str(i)
            self.dfs(n,k,i,path,results,1)

        for r in results:
            if int(r) not in re:
                re.append(int(r))
        print(re)
        return re
    def dfs(self,n,k,num,path,results,time):
        if time == n:
            results.append(path)
            return
        if num - k >= 0:
            self.dfs(n,k,num-k,path+str(num-k),results,time+1)

        if num + k <= 9:
            self.dfs(n,k,num+k,path+str(num+k),results,time+1)



if __name__ == "__main__":
    n = 3
    k = 7

    n = 2
    k = 1
    #
    n = 2
    k = 0

    n = 2
    k = 2
    solution = Solution()
    solution.numsSameConsecDiff(n,k)