class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """

        sig = sum(matchsticks) % 4
        if sig != 0:
            return False
        else:
            result = []
            bian = [0] * 4
            matchsticks.sort()
            self.dfs(matchsticks,int(sum(matchsticks)/4),bian,result)
            print(result)
            if len(result)!=0:
                return True
            else:
                return False


    def dfs(self,matchsticks,a,bian,result):
        if bian[0] == a and bian[1] == a and bian[2] == a and bian[3] == a:
            result.append(1)
            return

        for i in range(4):
            if matchsticks[0] <= a-bian[i]:
                bian[i] += matchsticks[0]
                self.dfs(matchsticks[1:],a,bian,result)
                bian[i] -= matchsticks[0]


if __name__ == '__main__':
    matchsticks = [1, 1, 2, 2, 2]
    matchsticks = [3, 3, 3, 3, 4]
    matchsticks = [1,1,1,1,1,2,2,3,4]

    solution = Solution()
    solution.makesquare(matchsticks)