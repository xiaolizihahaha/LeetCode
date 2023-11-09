class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if sum(matchsticks) % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        sig = self.dfs(matchsticks,[0] * 4,0,sum(matchsticks) // 4)
        print(sig)
        return sig

    def dfs(self,matchsticks,side,index,a):
        if index == len(matchsticks) and side[0] == a and side[1] == a and side[2] == a and side[3] == a:
            return True


        for i in range(4):
            # print(index)
            if matchsticks[index] <= a - side[i]:
                side[i] += matchsticks[index]
                if self.dfs(matchsticks,side,index+1,a) is True:
                    return True
                side[i] -=matchsticks[index]
            else:
                continue
        return False





if __name__ == '__main__':
    # matchsticks = [1, 1, 2, 2, 2]
    # matchsticks = [3, 3, 3, 3, 4]
    # matchsticks = [1,1,1,1,1,2,2,3,4]
    matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]

    solution = Solution()
    solution.makesquare(matchsticks)