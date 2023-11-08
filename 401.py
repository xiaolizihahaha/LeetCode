class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        h = [8,4,2,1]
        m = [32,16,8,4,2,1]
        results = list()
        ran = min(turnedOn,4)
        for i in range(ran+1):
            hs = []
            ms = []
            j = turnedOn - i
            if j >= 0 and j <= 6:

                print(i,j)
                self.dfs1(i,h,11,[],hs)
                self.dfs1(j,m,59,[],ms)
                for h1 in hs:
                    for m1 in ms:
                        temp = str(m1)
                        if m1 < 10:
                            temp = '0' + str(m1)
                        newthing = str(h1) + ':' + temp
                        results.append(newthing)

        print(results)
        return results
        # print(hs)
        # print(ms)



    def dfs1(self,n,h,max,path,result):
        if len(path) == n:
            if sum(path) <= max and sum(path) not in result:
                result.append(sum(path))
            return

        for index,val in enumerate(h):
            path.append(val)
            self.dfs1(n,h[index+1:],max,path,result)
            path.pop(-1)





if __name__ == '__main__':
    turnedOn = 9
    solution = Solution()
    solution.readBinaryWatch(turnedOn)